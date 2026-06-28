import numpy as np


class ImageNormalizer:

    @staticmethod
    def min_max(image):

        image = image.astype(np.float32)

        minimum = image.min()
        maximum = image.max()

        if maximum == minimum:
            return np.zeros_like(image, dtype=np.float32)

        return (image - minimum) / (maximum - minimum)

    @staticmethod
    def percentile(image, low=2, high=98):

        image = image.astype(np.float32)

        p_low = np.percentile(image, low)
        p_high = np.percentile(image, high)

        image = np.clip(image, p_low, p_high)

        return (image - p_low) / (p_high - p_low + 1e-8)