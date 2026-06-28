import numpy as np
from skimage.feature import local_binary_pattern


class TextureFeatures:

    @staticmethod
    def lbp(image, radius=1):

        image = (image * 255).astype(np.uint8)

        n_points = 8 * radius

        lbp = local_binary_pattern(
            image,
            n_points,
            radius,
            method="uniform"
        )

        lbp = lbp.astype(np.float32)

        lbp = (lbp - lbp.min()) / (lbp.max() - lbp.min() + 1e-8)

        return lbp

    @staticmethod
    def entropy(image):

        image = image.astype(np.float32)

        hist, _ = np.histogram(image, bins=256)

        p = hist / np.sum(hist)

        p = p[p > 0]

        return -np.sum(p * np.log2(p))

    @staticmethod
    def variance(image):

        return float(np.var(image))