import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import numpy as np
import matplotlib.pyplot as plt

from data_processing.binary_image_reader import BinaryImageReader

from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter

from feature_extraction.edge_detector import EdgeDetector

from crater_detection.crater_candidates import CraterCandidates

from landing_site.terrain_roughness import TerrainRoughness
from landing_site.hazard_map import HazardMap


reader = BinaryImageReader()

img_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img_path, xml_path)

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

candidates = CraterCandidates().extract(edges)

roughness = TerrainRoughness().compute(clean)

hazard = HazardMap().generate(roughness, candidates)

plt.figure(figsize=(14,6))

plt.subplot(121)
plt.imshow(clean, cmap="gray")
plt.title("Input")

plt.subplot(122)
plt.imshow(hazard)
plt.title("Hazard Map")

plt.tight_layout()
plt.show()

print("\n===================================")
print("Hazard Map Generated Successfully")
print("===================================")
print("Detected Hazard Zones :", len(candidates))