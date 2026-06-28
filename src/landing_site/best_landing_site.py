import cv2
import numpy as np


class BestLandingSite:

    def find(self, suitability_map):

        blur = cv2.GaussianBlur(suitability_map, (51, 51), 0)

        _, maxVal, _, maxLoc = cv2.minMaxLoc(blur)

        return maxLoc, maxVal