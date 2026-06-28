import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import numpy as np

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter

from landing_site.terrain_roughness import TerrainRoughness
from ice_detection.ice_probability import IceProbability

from sar.sar_reader import SARReader
from sar.backscatter import Backscatter

from fusion.feature_fusion import FeatureFusion
from ice_detection.ice_candidate_detector import IceCandidateDetector
from ice_detection.ice_volume_estimator import IceVolumeEstimator


# ---------------- OHRC ----------------

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

roughness = TerrainRoughness().compute(clean)
ice = IceProbability().estimate(clean)

# ---------------- SAR ----------------

sar_reader = SARReader()

dat = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.dat"

sar_xml = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.xml"

sar = sar_reader.read(dat, sar_xml)

sar_crop = sar[10000:11000, 500:1500]

backscatter = Backscatter().compute(sar_crop)

# ---------------- Feature Fusion ----------------

features = FeatureFusion().fuse(
    clean,
    roughness,
    ice,
    backscatter
)

score, mask = IceCandidateDetector().detect(features)

# ---------------- Ice Volume ----------------
result = IceVolumeEstimator().estimate(
    mask,
    score,
    pixel_resolution=0.21,
    estimated_thickness=2.0
)

print("\n==============================")
print("ICE VOLUME ESTIMATION")
print("==============================")

for key, value in result.items():
    print(f"{key:25}: {value}")
