import numpy as np


class IceVolumeEstimator:

    def estimate(
        self,
        ice_mask,
        ice_score,
        pixel_resolution=0.21,
        estimated_thickness=2.0
    ):

        ice_pixels = int(np.sum(ice_mask > 0))

        pixel_area = pixel_resolution * pixel_resolution

        area = ice_pixels * pixel_area

        volume = area * estimated_thickness

        confidence = float(np.mean(ice_score[ice_mask > 0]) * 100) \
            if ice_pixels > 0 else 0

        if volume < 2000:
            category = "Very Low"

        elif volume < 5000:
            category = "Low"

        elif volume < 10000:
            category = "Moderate"

        elif volume < 20000:
            category = "High"

        else:
            category = "Very High"

        return {
            "ice_pixels": ice_pixels,
            "pixel_area_m2": round(pixel_area, 4),
            "ice_area_m2": round(area, 2),
            "estimated_thickness_m": estimated_thickness,
            "estimated_volume_m3": round(volume, 2),
            "confidence_percent": round(confidence, 2),
            "resource_category": category
        }