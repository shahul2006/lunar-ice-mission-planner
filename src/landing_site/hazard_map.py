import cv2
import numpy as np


class HazardMap:

    def generate(self, roughness, crater_candidates):

        hazard = cv2.cvtColor(roughness, cv2.COLOR_GRAY2BGR)

        # Red = High Hazard
        hazard[:, :, 2] = roughness

        # Green = Safe
        hazard[:, :, 1] = 255 - roughness

        # Blue = Unused
        hazard[:, :, 0] = 0

        # Mark crater hazard zones
        for x, y, r, _ in crater_candidates:
            cv2.circle(hazard, (x, y), r + 20, (255, 0, 255), -1)

        return hazard