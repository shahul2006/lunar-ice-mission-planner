import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import numpy as np
import matplotlib.pyplot as plt

from sar.sar_reader import SARReader


reader = SARReader()

dat = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.dat"

xml = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.xml"

sar = reader.read(dat, xml)

print("\nShape :", sar.shape)
print("Minimum :", sar.min())
print("Maximum :", sar.max())

crop = sar[10000:11000, 500:1500].astype(np.float32)

crop = np.abs(crop)

crop = (crop-crop.min())/(crop.max()-crop.min()+1e-8)

plt.figure(figsize=(8,8))
plt.imshow(crop, cmap="gray")
plt.title("SAR Preview")
plt.axis("off")
plt.show()