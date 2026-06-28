import cv2
import numpy as np


class CraterDetector:

    def __init__(self):
        pass

    def detect(self, image):

        # convert to uint8
        img = image.copy()

        if img.dtype != np.uint8:
            img = cv2.normalize(
                img,
                None,
                0,
                255,
                cv2.NORM_MINMAX
            ).astype(np.uint8)

        # remove noise
        blur = cv2.GaussianBlur(img, (5, 5), 1.5)

        circles = cv2.HoughCircles(
            blur,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=40,
            param1=100,
            param2=25,
            minRadius=5,
            maxRadius=80
        )

        output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        crater_count = 0

        if circles is not None:

            circles = np.round(circles[0]).astype(int)

            crater_count = len(circles)

            for x, y, r in circles:

                cv2.circle(
                    output,
                    (x, y),
                    r,
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    output,
                    (x, y),
                    2,
                    (255, 0, 0),
                    3
                )

        return output, crater_count