import numpy as np
import cv2


class Backscatter:

    def compute(self, sar):

        image = sar.astype(np.float32)

        # Amplitude
        image = np.abs(image)

        # Log compression
        image = np.log1p(image)

        # Robust normalization
        low = np.percentile(image, 2)
        high = np.percentile(image, 98)

        image = np.clip(image, low, high)

        image = (image - low) / (high - low + 1e-8)

        image = (image * 255).astype(np.uint8)

        return image