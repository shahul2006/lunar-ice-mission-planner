import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
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

from dashboard.mission_dashboard import MissionDashboard


# ----------------------------------------------------
# Load Image
# ----------------------------------------------------

reader = BinaryImageReader()

img_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img_path, xml_path)

crop = image[30000:31000,5000:6000]

crop = crop.astype(np.float32)

low = np.percentile(crop,2)
high = np.percentile(crop,98)

crop = np.clip(crop,low,high)
crop = (crop-low)/(high-low)
crop = (crop*255).astype(np.uint8)


# ----------------------------------------------------
# Preprocessing
# ----------------------------------------------------

clean = Destriper().remove_vertical_stripes(crop)

clean = NoiseFilter().gaussian(clean)


# ----------------------------------------------------
# Edge Detection
# ----------------------------------------------------

edges = EdgeDetector().canny(clean)


# ----------------------------------------------------
# Crater Detection
# ----------------------------------------------------

candidates = CraterCandidates().extract(edges)


# ----------------------------------------------------
# Terrain Analysis
# ----------------------------------------------------

roughness = TerrainRoughness().compute(clean)


# ----------------------------------------------------
# Ice Probability
# ----------------------------------------------------

ice = IceProbability().estimate(clean)


# ----------------------------------------------------
# Landing Suitability
# ----------------------------------------------------

landing = LandingSuitability().compute(
    roughness,
    candidates
)


# ----------------------------------------------------
# Best Landing Site
# ----------------------------------------------------

best_point, score = BestLandingSite().find(landing)


# ----------------------------------------------------
# Hazard Map
# ----------------------------------------------------

hazard = HazardMap().generate(
    roughness,
    candidates
)


# ----------------------------------------------------
# Rover Path
# ----------------------------------------------------

cost = 255 - landing

planner = AStarPlanner()

start = (best_point[1], best_point[0])

goal = (100,100)

path = planner.search(
    cost.astype(np.float32),
    start,
    goal
)

rover = cv2.cvtColor(clean,cv2.COLOR_GRAY2BGR)

for r,c in path:
    cv2.circle(rover,(c,r),1,(255,0,0),-1)

cv2.circle(
    rover,
    (best_point[0],best_point[1]),
    8,
    (0,255,0),
    -1
)


# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

MissionDashboard().show(

    original=clean,

    roughness=roughness,

    ice=ice,

    landing=landing,

    hazard=hazard,

    rover=rover
)


print("\n==============================")
print("MISSION COMPLETED")
print("==============================")
print("Detected Craters :", len(candidates))
print("Landing Site     :", best_point)
print("Safety Score     :", score)
print("Rover Path Nodes :", len(path))