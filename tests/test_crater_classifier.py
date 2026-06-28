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
from feature_extraction.edge_detector import EdgeDetector

from crater_detection.crater_candidates import CraterCandidates
from crater_detection.crater_classifier import CraterClassifier


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

classified = CraterClassifier().classify(candidates)

output = cv2.cvtColor(clean, cv2.COLOR_GRAY2BGR)

for crater in classified:

    x, y = crater["center"]
    r = crater["radius"]

    cv2.circle(output, (x, y), r, (0, 255, 0), 2)

    cv2.putText(
        output,
        crater["size"],
        (x + 5, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.4,
        (255, 0, 0),
        1,
    )

print("\nDetected Craters\n")

for crater in classified:
    print(crater)

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(clean, cmap="gray")
plt.title("Input")

plt.subplot(122)
plt.imshow(output)
plt.title("Classified Craters")

plt.tight_layout()
plt.show()