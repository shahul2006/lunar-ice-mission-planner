from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.binary_image_reader import BinaryImageReader

PROJECT_ROOT = Path(__file__).resolve().parents[2]

reader = BinaryImageReader()

image_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(image_path, xml_path)

fig, ax = plt.subplots(2, 2, figsize=(12, 12))

crops = [
    image[0:1000, 0:1000],
    image[25000:26000, 3000:4000],
    image[50000:51000, 6000:7000],
    image[90000:91000, 10000:11000]
]

titles = [
    "Top Left",
    "Upper Middle",
    "Center",
    "Bottom Right"
]

for a, c, t in zip(ax.ravel(), crops, titles):
    c = c.astype(np.float32)

    low = np.percentile(c, 2)
    high = np.percentile(c, 98)

    c = np.clip(c, low, high)
    c = (c - low) / (high - low + 1e-8)

    a.imshow(c, cmap="gray")
    a.set_title(t)
    a.axis("off")

plt.tight_layout()
plt.show()