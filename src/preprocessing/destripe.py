import numpy as np
import matplotlib.pyplot as plt


class Destriper:

    def __init__(self):
        pass

    def remove_vertical_stripes(self, image):

        img = image.astype(np.float32)

        # Mean intensity of each column
        column_mean = np.mean(img, axis=0)

        # Overall image mean
        overall_mean = np.mean(column_mean)

        # Compute correction for each column
        correction = column_mean - overall_mean

        # Remove striping
        corrected = img - correction

        corrected = np.clip(corrected, 0, 255)

        return corrected.astype(np.uint8)