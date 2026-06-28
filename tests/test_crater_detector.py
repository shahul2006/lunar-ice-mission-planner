import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

import numpy as np
import matplotlib.pyplot as plt

from data_processing.binary_image_reader import BinaryImageReader
from crater_detection.crater_detector import CraterDetector


reader = BinaryImageReader()

img_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img_path, xml_path)

# crop a region
crop = image[30000:31000, 5000:6000]

crop = crop.astype(np.float32)

low = np.percentile(crop, 2)
high = np.percentile(crop, 98)

crop = np.clip(crop, low, high)
crop = (crop - low) / (high - low)

crop = (crop * 255).astype(np.uint8)


detector = CraterDetector()

result, count = detector.detect(crop)

print("\nDetected Craters :", count)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(crop, cmap="gray")
plt.title("Input")

plt.subplot(1,2,2)
plt.imshow(result)
plt.title(f"Detected Craters : {count}")

plt.tight_layout()
plt.show()