import cv2
import numpy as np


class IceProbability:

    def estimate(self, image):

        image = image.astype(np.float32)

        image = cv2.GaussianBlur(image, (5, 5), 0)

        image = cv2.normalize(
            image,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        probability = 255 - image

        return probability.astype(np.uint8)