import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import numpy as np
import matplotlib.pyplot as plt

from data_processing.binary_image_reader import BinaryImageReader
from preprocessing.destripe import Destriper
from preprocessing.noise_filter import NoiseFilter
from feature_extraction.edge_detector import EdgeDetector

reader = BinaryImageReader()

img_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(img_path, xml_path)

crop = image[30000:31000,5000:6000]

crop = crop.astype(np.float32)

low = np.percentile(crop,2)
high = np.percentile(crop,98)

crop = np.clip(crop, low, high)
crop = (crop-low)/(high-low)
crop = (crop*255).astype(np.uint8)

destriper = Destriper()
clean = destriper.remove_vertical_stripes(crop)

noise = NoiseFilter()
clean = noise.gaussian(clean)

edge = EdgeDetector()
edges = edge.canny(clean)

plt.figure(figsize=(12,4))

plt.subplot(131)
plt.imshow(crop, cmap="gray")
plt.title("Original")

plt.subplot(132)
plt.imshow(clean, cmap="gray")
plt.title("Filtered")

plt.subplot(133)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edges")

plt.tight_layout()
plt.show()