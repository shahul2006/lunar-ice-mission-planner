import numpy as np


class IceCandidateDetector:

    def detect(self, features):

        # Channel mapping
        ohrc = features[:, :, 0].astype(np.float32)
        roughness = features[:, :, 1].astype(np.float32)
        ice = features[:, :, 2].astype(np.float32)
        sar = features[:, :, 3].astype(np.float32)

        # Normalize
        roughness /= 255.0
        ice /= 255.0
        sar /= 255.0

        # Ice Score
        score = (
            0.45 * sar +
            0.35 * ice +
            0.20 * (1 - roughness)
        )

        threshold = np.percentile(score, 90)

        mask = (score >= threshold).astype(np.uint8)
        return score, mask