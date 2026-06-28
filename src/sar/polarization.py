import numpy as np


class PolarizationFeatures:

    def compute(self, image):

        image = image.astype(np.float32)

        mean = np.mean(image)
        std = np.std(image)
        minimum = np.min(image)
        maximum = np.max(image)

        return {
            "mean": float(mean),
            "std": float(std),
            "min": float(minimum),
            "max": float(maximum),
        }