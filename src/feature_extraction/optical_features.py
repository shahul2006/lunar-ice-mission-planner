import cv2
import numpy as np


class OpticalFeatures:

    @staticmethod
    def mean(image):
        return float(np.mean(image))

    @staticmethod
    def std(image):
        return float(np.std(image))

    @staticmethod
    def sobel(image):

        image = image.astype(np.float32)

        gx = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
        gy = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)

        gradient = np.sqrt(gx**2 + gy**2)

        gradient = cv2.normalize(
            gradient,
            None,
            0,
            1,
            cv2.NORM_MINMAX
        )

        return gradient