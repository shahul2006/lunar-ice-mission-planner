from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from binary_image_reader import BinaryImageReader

PROJECT_ROOT = Path(__file__).resolve().parents[2]

reader = BinaryImageReader()

image_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(image_path, xml_path)

print("\nImage Statistics")
print("-" * 40)
print("Shape :", image.shape)
print("Minimum :", image.min())
print("Maximum :", image.max())
print("Mean :", image.mean())

# -------------------------------------------------
# Display only a small crop
# -------------------------------------------------

crop = image[0:1000, 0:1000]

plt.figure(figsize=(8,8))
plt.imshow(crop, cmap="gray")
plt.title("OHRC Scene 01 - Crop")
plt.colorbar()
plt.show()