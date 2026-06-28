from pathlib import Path
import sys
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.normalize import ImageNormalizer

reader = BinaryImageReader()

img = reader.read(
    PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img",
    PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"
)

crop = img[50000:51000, 5000:6000]

normalized = ImageNormalizer.percentile(crop)

plt.figure(figsize=(8,8))
plt.imshow(normalized, cmap="gray")
plt.title("Normalized OHRC")
plt.axis("off")
plt.show()