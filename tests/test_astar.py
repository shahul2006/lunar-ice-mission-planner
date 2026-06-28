import sys
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.binary_image_reader import BinaryImageReader
from path_planning.astar import AStarPlanner


# --------------------------------------------------
# Load OHRC Image
# --------------------------------------------------

reader = BinaryImageReader()

image_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.img"

xml_path = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

image = reader.read(image_path, xml_path)

crop = image[0:1000, 0:1000].astype(np.float32)

crop = (crop - crop.min()) / (crop.max() - crop.min())

# --------------------------------------------------
# Hazard / Cost Map
# --------------------------------------------------

blur = cv2.GaussianBlur(crop, (5, 5), 0)

grad_x = cv2.Sobel(blur, cv2.CV_32F, 1, 0)
grad_y = cv2.Sobel(blur, cv2.CV_32F, 0, 1)

roughness = cv2.magnitude(grad_x, grad_y)

roughness = cv2.normalize(
    roughness,
    None,
    1,
    50,
    cv2.NORM_MINMAX
)

cost_map = roughness.astype(np.float32)

# --------------------------------------------------
# Start & Goal
# --------------------------------------------------

start = (100, 100)
goal = (850, 850)

planner = AStarPlanner()

path = planner.search(cost_map, start, goal)

print("\nPath Length :", len(path))

# --------------------------------------------------
# Visualization
# --------------------------------------------------

display = cv2.cvtColor((crop * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)

for r, c in path:
    cv2.circle(display, (c, r), 1, (0, 0, 255), -1)

cv2.circle(display, (start[1], start[0]), 8, (0, 255, 0), -1)
cv2.circle(display, (goal[1], goal[0]), 8, (255, 0, 0), -1)

plt.figure(figsize=(8, 8))
plt.imshow(cv2.cvtColor(display, cv2.COLOR_BGR2RGB))
plt.title("A* Rover Path Planning")
plt.axis("off")
plt.show()
