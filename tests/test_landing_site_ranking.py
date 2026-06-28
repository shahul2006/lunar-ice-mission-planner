import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import cv2
import numpy as np
import matplotlib.pyplot as plt

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter

from landing_site.terrain_roughness import TerrainRoughness
from landing_site.landing_suitability import LandingSuitability
from crater_detection.crater_candidates import CraterCandidates
from feature_extraction.edge_detector import EdgeDetector

from landing_site.landing_site_ranking import LandingSiteRanking


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

sites = ranking.rank(landing, top_k=10)

display = cv2.cvtColor(clean, cv2.COLOR_GRAY2BGR)

for i, site in enumerate(sites):

    x = site["x"]
    y = site["y"]

    cv2.circle(display, (x, y), 8, (0,255,0), 2)

    cv2.putText(
        display,
        str(i+1),
        (x+10, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255,0,0),
        1
    )

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(display, cv2.COLOR_BGR2RGB))
plt.title("Top 10 Landing Sites")
plt.axis("off")
plt.show()

print("\n==============================")
print("TOP LANDING SITES")
print("==============================")

for i, site in enumerate(sites):
    print(
        f"{i+1:2d}. "
        f"({site['x']}, {site['y']}) "
        f"Score = {site['score']:.2f}"
    )