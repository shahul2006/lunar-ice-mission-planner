from pathlib import Path
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[2]

xml_path = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.xml"
dat_path = PROJECT_ROOT / "data/raw/SAR/Scene_01/data/raw/20251106/ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.dat"

# -------------------------
# Read XML
# -------------------------
tree = ET.parse(xml_path)
root = tree.getroot()

ns = {"pds": "http://pds.nasa.gov/pds4/pds/v1"}

lines = int(root.find(".//pds:Axis_Array[pds:axis_name='Line']/pds:elements", ns).text)
samples = int(root.find(".//pds:Axis_Array[pds:axis_name='Sample']/pds:elements", ns).text)

print("="*60)
print("SAR METADATA")
print("="*60)
print("Lines   :", lines)
print("Samples :", samples)

# -------------------------
# Read only first 1000 lines
# -------------------------
rows = 1000

image = np.memmap(
    dat_path,
    dtype=np.int8,
    mode="r",
    shape=(lines, samples)
)

crop = image[:rows, :]

print("\nCrop Shape :", crop.shape)
print("Minimum    :", crop.min())
print("Maximum    :", crop.max())
print("Mean       :", crop.mean())

# -------------------------
# Display
# -------------------------
display = crop.astype(np.float32)

display = (display - display.min()) / (display.max() - display.min() + 1e-8)

plt.figure(figsize=(10,6))
plt.imshow(display, cmap="gray", aspect="auto")
plt.title("SAR Scene 01 - First 1000 Lines")
plt.xlabel("Samples")
plt.ylabel("Lines")
plt.colorbar()
plt.show()