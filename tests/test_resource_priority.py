import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from data_processing.binary_image_reader import BinaryImageReader

from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter

from landing_site.terrain_roughness import TerrainRoughness
from ice_detection.ice_probability import IceProbability

from sar.sar_reader import SARReader
from sar.backscatter import Backscatter

from fusion.feature_fusion import FeatureFusion

from ice_detection.ice_candidate_detector import IceCandidateDetector

from landing_site.landing_site_ranking import LandingSiteRanking
from landing_site.landing_suitability import LandingSuitability

from crater_detection.crater_candidates import CraterCandidates
from feature_extraction.edge_detector import EdgeDetector

from ice_detection.resource_priority import ResourcePriority

import numpy as np


reader = BinaryImageReader()

img = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img, xml)

crop = image[30000:31000, 5000:6000]

crop = crop.astype(np.float32)

low = np.percentile(crop, 2)
high = np.percentile(crop, 98)

crop = np.clip(crop, low, high)
crop = (crop - low) / (high - low)
crop = (crop * 255).astype(np.uint8)

clean = Destriper().remove_vertical_stripes(crop)
clean = NoiseFilter().gaussian(clean)

edges = EdgeDetector().canny(clean)

craters = CraterCandidates().extract(edges)

roughness = TerrainRoughness().compute(clean)

landing = LandingSuitability().compute(
    roughness,
    craters
)

ranking = LandingSiteRanking()

landing_site = ranking.rank(landing)[0]

landing_xy = (
    landing_site["x"],
    landing_site["y"]
)

sar_reader = SARReader()

dat = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.dat"

sar_xml = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.xml"

sar = sar_reader.read(dat, sar_xml)

sar_crop = sar[10000:11000, 500:1500]

backscatter = Backscatter().compute(sar_crop)

features = FeatureFusion().fuse(
    clean,
    roughness,
    IceProbability().estimate(clean),
    backscatter
)

score, mask = IceCandidateDetector().detect(features)

resources = ResourcePriority().rank(
    mask,
    score,
    landing_xy
)

print("\n==============================")
print("RESOURCE PRIORITY")
print("==============================")

for i, resource in enumerate(resources[:10], start=1):
    print(f"\nRank {i}")
    for key, value in resource.items():
        print(f"{key:18}: {value}")