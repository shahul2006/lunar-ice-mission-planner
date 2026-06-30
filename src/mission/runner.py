from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import cv2
import numpy as np

from data_processing.binary_image_reader import BinaryImageReader

from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter

from feature_extraction.edge_detector import EdgeDetector

from crater_detection.crater_candidates import CraterCandidates

from landing_site.terrain_roughness import TerrainRoughness
from landing_site.landing_suitability import LandingSuitability
from landing_site.best_landing_site import BestLandingSite
from landing_site.hazard_map import HazardMap

from ice_detection.ice_probability import IceProbability

from path_planning.astar import AStarPlanner


class MissionRunner:

    def run(self, img_path, xml_path):

        # ---------------------------------------------
        # Load Image
        # ---------------------------------------------
        reader = BinaryImageReader()

        image = reader.read(img_path, xml_path)

        # Crop Region
        crop = image[30000:31000, 5000:6000]

        crop = crop.astype(np.float32)

        low = np.percentile(crop, 2)
        high = np.percentile(crop, 98)

        # Clip extreme values
        crop = np.clip(crop, low, high)

        # Normalize
        crop = cv2.normalize(
            crop,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        ).astype(np.uint8)

        # CLAHE Contrast Enhancement
        clahe = cv2.createCLAHE(
            clipLimit=3.0,
            tileGridSize=(8, 8)
        )

        crop = clahe.apply(crop)

        # Sharpen Image
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        crop = cv2.filter2D(
            crop,
            -1,
            kernel
        )

        # ---------------------------------------------
        # Preprocessing
        # ---------------------------------------------
        clean = Destriper().remove_vertical_stripes(crop)

        clean = NoiseFilter().gaussian(clean)

        # ---------------------------------------------
        # Edge Detection
        # ---------------------------------------------
        edges = EdgeDetector().canny(clean)

        # ---------------------------------------------
        # Crater Candidates
        # ---------------------------------------------
        candidates = CraterCandidates().extract(edges)

        # ---------------------------------------------
        # Terrain Roughness
        # ---------------------------------------------
        roughness = TerrainRoughness().compute(clean)

        # ---------------------------------------------
        # Ice Probability
        # ---------------------------------------------
        ice = IceProbability().estimate(clean)

        # ---------------------------------------------
        # Landing Suitability
        # ---------------------------------------------
        landing = LandingSuitability().compute(
            roughness,
            candidates
        )

        # ---------------------------------------------
        # Best Landing Site
        # ---------------------------------------------
        best_point, score = BestLandingSite().find(
            landing
        )

        # ---------------------------------------------
        # Hazard Map
        # ---------------------------------------------
        hazard = HazardMap().generate(
            roughness,
            candidates
        )

        # ---------------------------------------------
        # Rover Path
        # ---------------------------------------------
        cost = 255 - landing

        planner = AStarPlanner()

        start = (best_point[1], best_point[0])
        goal = (100, 100)

        path = planner.search(
            cost.astype(np.float32),
            start,
            goal
        )

        rover = cv2.cvtColor(
            clean,
            cv2.COLOR_GRAY2BGR
        )

        for r, c in path:
            cv2.circle(
                rover,
                (c, r),
                2,
                (0, 0, 255),
                -1
            )

        cv2.circle(
            rover,
            (best_point[0], best_point[1]),
            8,
            (0, 255, 0),
            -1
        )

        # ---------------------------------------------
        # Better Display Images
        # ---------------------------------------------
        ohrc_display = cv2.normalize(
            clean,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        ohrc_display = cv2.GaussianBlur(
            ohrc_display,
            (3, 3),
            0
        )

        clahe = cv2.createCLAHE(
            clipLimit=2.5,
            tileGridSize=(8, 8)
        )

        ohrc_display = clahe.apply(
            ohrc_display.astype(np.uint8)
        )

        ice_display = cv2.applyColorMap(
            ice,
            cv2.COLORMAP_JET
        )

        hazard_display = cv2.applyColorMap(
            hazard,
            cv2.COLORMAP_TURBO
        )
                # ---------------------------------------------
        # Save Images
        # ---------------------------------------------
        output_dir = PROJECT_ROOT / "outputs"
        output_dir.mkdir(exist_ok=True)

        cv2.imwrite(
            str(output_dir / "ohrc.png"),
            ohrc_display
        )

        cv2.imwrite(
            str(output_dir / "ice_probability.png"),
            ice_display
        )

        cv2.imwrite(
            str(output_dir / "hazard_map.png"),
            hazard_display
        )

        cv2.imwrite(
            str(output_dir / "rover_path.png"),
            rover
        )

        # ---------------------------------------------
        # Mission Statistics
        # ---------------------------------------------

        # Number of high-probability ice pixels
        ice_pixels = int(np.sum(ice > 200))

        # Approximate ice volume
        # (Replace with scientific conversion later)
        ice_volume = round(ice_pixels * 0.25, 2)

        # Number of hazard zones
        # (Each detected crater is treated as one hazard)
        hazard_zones = len(candidates)

        # ---------------------------------------------
        # Return Results
        # ---------------------------------------------
        return {
            "landing_site": list(best_point),
            "mission_score": float(score),
            "crater_count": int(len(candidates)),
            "path_length": int(len(path)),
            "ice_volume": float(ice_volume),
            "hazard_zones": int(hazard_zones),
        }