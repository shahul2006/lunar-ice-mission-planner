from pathlib import Path
import sys
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.normalize import ImageNormalizer
from feature_extraction.optical_features import OpticalFeatures

reader = BinaryImageReader()

img = reader.read(
    PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img",
    PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"
)

crop = img[50000:51000, 5000:6000]

crop = ImageNormalizer.percentile(crop)

edges = OpticalFeatures.sobel(crop)

print("Mean :", OpticalFeatures.mean(crop))
print("Std  :", OpticalFeatures.std(crop))

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(crop, cmap="gray")
plt.title("Normalized")

plt.subplot(1,2,2)
plt.imshow(edges, cmap="gray")
plt.title("Sobel Gradient")

plt.tight_layout()
plt.show()