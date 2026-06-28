from pathlib import Path
import sys
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.normalize import ImageNormalizer
from feature_extraction.texture_features import TextureFeatures

reader = BinaryImageReader()

img = reader.read(
    PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img",
    PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"
)

crop = img[50000:51000, 5000:6000]

crop = ImageNormalizer.percentile(crop)

lbp = TextureFeatures.lbp(crop)

print("\nTexture Statistics")
print("-" * 30)
print("Entropy :", TextureFeatures.entropy(crop))
print("Variance:", TextureFeatures.variance(crop))

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(crop, cmap="gray")
plt.title("Normalized")

plt.subplot(1,2,2)
plt.imshow(lbp, cmap="gray")
plt.title("LBP Texture")

plt.tight_layout()
plt.show()