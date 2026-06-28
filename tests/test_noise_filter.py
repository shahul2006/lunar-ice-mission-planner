import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import numpy as np
import matplotlib.pyplot as plt

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter

reader = BinaryImageReader()

img_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img_path, xml_path)

crop = image[30000:31000,5000:6000]

crop = crop.astype(np.float32)

low = np.percentile(crop,2)
high = np.percentile(crop,98)

crop = np.clip(crop,low,high)
crop = (crop-low)/(high-low)
crop = (crop*255).astype(np.uint8)

destriper = Destriper()
clean = destriper.remove_vertical_stripes(crop)

filter = NoiseFilter()

median = filter.median(clean)
gaussian = filter.gaussian(clean)
bilateral = filter.bilateral(clean)

plt.figure(figsize=(14,8))

plt.subplot(221)
plt.imshow(clean,cmap="gray")
plt.title("Destriped")

plt.subplot(222)
plt.imshow(median,cmap="gray")
plt.title("Median")

plt.subplot(223)
plt.imshow(gaussian,cmap="gray")
plt.title("Gaussian")

plt.subplot(224)
plt.imshow(bilateral,cmap="gray")
plt.title("Bilateral")

plt.tight_layout()
plt.show()