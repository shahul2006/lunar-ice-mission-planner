import cv2
import numpy as np


class TerrainRoughness:

    def compute(self, image):

        image = image.astype(np.float32)

        lap = cv2.Laplacian(image, cv2.CV_32F)

        roughness = np.abs(lap)

        roughness = cv2.normalize(
            roughness,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        return roughness.astype(np.uint8)