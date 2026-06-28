import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import matplotlib.pyplot as plt
import numpy as np

from tmc.tmc_reader import TMCReader


reader = TMCReader()

img = PROJECT_ROOT / "data/raw/TMC-2/Scene_02/data/calibrated/20251107/ch2_tmc_ncn_20251107T2205342105_d_img_d18.img"

xml = PROJECT_ROOT / "data/raw/TMC-2/Scene_02/data/calibrated/20251107/ch2_tmc_ncn_20251107T2205342105_d_img_d18.xml"

image = reader.read(img, xml)

crop = image[20000:21000, 1000:2000]

crop = crop.astype(np.float32)

low = np.percentile(crop, 2)
high = np.percentile(crop, 98)

crop = np.clip(crop, low, high)
crop = (crop - low) / (high - low)

plt.figure(figsize=(8,8))
plt.imshow(crop, cmap="gray")
plt.title("TMC Scene 02")
plt.axis("off")
plt.show()