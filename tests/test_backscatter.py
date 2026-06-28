import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import matplotlib.pyplot as plt

from sar.sar_reader import SARReader
from sar.backscatter import Backscatter

reader = SARReader()

dat = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.dat"

xml = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.xml"

sar = reader.read(dat, xml)

# Small crop for visualization
crop = sar[10000:11000, 500:1500]

backscatter = Backscatter().compute(crop)

plt.figure(figsize=(8, 8))
plt.imshow(backscatter, cmap="gray")
plt.title("SAR Backscatter")
plt.axis("off")
plt.show()

print("\n========== BACKSCATTER ==========")
print("Min :", backscatter.min())
print("Max :", backscatter.max())
print("Mean:", backscatter.mean())