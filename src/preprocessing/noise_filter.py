import cv2
import numpy as np


class NoiseFilter:

    def __init__(self):
        pass

    def median(self, image):
        return cv2.medianBlur(image, 5)

    def gaussian(self, image):
        return cv2.GaussianBlur(image, (5,5), 1.2)

    def bilateral(self, image):
        return cv2.bilateralFilter(
            image,
            d=9,
            sigmaColor=75,
            sigmaSpace=75
        )