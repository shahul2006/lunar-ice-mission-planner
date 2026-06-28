import cv2
import numpy as np


class LandingSiteRanking:

    def rank(self, landing_map, top_k=10):

        image = landing_map.copy().astype(np.uint8)

        blur = cv2.GaussianBlur(image, (21, 21), 0)

        points = []

        temp = blur.copy()

        for _ in range(top_k):

            _, maxVal, _, maxLoc = cv2.minMaxLoc(temp)

            points.append({
                "x": maxLoc[0],
                "y": maxLoc[1],
                "score": float(maxVal)
            })

            cv2.circle(temp, maxLoc, 40, 0, -1)

        return points