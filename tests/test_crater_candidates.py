import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import numpy as np
import matplotlib.pyplot as plt
import cv2

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter
from feature_extraction.edge_detector import EdgeDetector
from crater_detection.crater_candidates import CraterCandidates


reader = BinaryImageReader()

img_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img_path, xml_path)

crop = image[30000:31000,5000:6000]

crop = crop.astype(np.float32)

low = np.percentile(crop,2)
high = np.percentile(crop,98)

crop = np.clip(crop, low, high)
crop = (crop-low)/(high-low)
crop = (crop*255).astype(np.uint8)

clean = Destriper().remove_vertical_stripes(crop)
clean = NoiseFilter().gaussian(clean)

edges = EdgeDetector().canny(clean)

detector = CraterCandidates()

craters = detector.extract(edges)

output = cv2.cvtColor(clean, cv2.COLOR_GRAY2BGR)

for x, y, r, c in craters:
    cv2.circle(output, (x, y), r, (0,255,0), 2)

print("Detected crater candidates:", len(craters))

plt.figure(figsize=(12,5))

plt.subplot(121)
plt.imshow(edges, cmap="gray")
plt.title("Edges")

plt.subplot(122)
plt.imshow(output)
plt.title(f"Candidates : {len(craters)}")

plt.tight_layout()
plt.show()