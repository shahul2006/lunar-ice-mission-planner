import cv2
import numpy as np


class LandingSuitability:

    def compute(self, roughness, crater_candidates):

        score = 255 - roughness.copy()

        for x, y, r, _ in crater_candidates:
            cv2.circle(score, (x, y), r + 15, 0, -1)

        return score