import numpy as np


class FeatureFusion:

    def fuse(
        self,
        ohrc,
        roughness,
        ice_probability,
        sar_backscatter
    ):

        h = min(
            ohrc.shape[0],
            roughness.shape[0],
            ice_probability.shape[0],
            sar_backscatter.shape[0]
        )

        w = min(
            ohrc.shape[1],
            roughness.shape[1],
            ice_probability.shape[1],
            sar_backscatter.shape[1]
        )

        ohrc = ohrc[:h, :w]
        roughness = roughness[:h, :w]
        ice_probability = ice_probability[:h, :w]
        sar_backscatter = sar_backscatter[:h, :w]

        fused = np.dstack([
            ohrc,
            roughness,
            ice_probability,
            sar_backscatter
        ])

        print("\n==============================")
        print("FEATURE FUSION COMPLETED")
        print("==============================")
        print("Shape :", fused.shape)

        return fused