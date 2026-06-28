import cv2
import numpy as np


class ResourcePriority:

    def rank(
        self,
        ice_mask,
        ice_score,
        landing_site
    ):

        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            ice_mask.astype(np.uint8),
            connectivity=8
        )

        resources = []

        for i in range(1, num_labels):

            area = stats[i, cv2.CC_STAT_AREA]

            if area < 10:
                continue

            cx, cy = centroids[i]

            confidence = np.mean(
                ice_score[labels == i]
            ) * 100

            distance = np.sqrt(
                (cx - landing_site[0]) ** 2 +
                (cy - landing_site[1]) ** 2
            )

            priority = (
                area * 0.5 +
                confidence * 0.4 -
                distance * 0.1
            )

            resources.append({

                "id": i,

                "center": (
                    int(cx),
                    int(cy)
                ),

                "area_pixels": int(area),

                "confidence": round(float(confidence), 2),

                "distance_pixels": round(float(distance), 2),

                "priority_score": round(float(priority), 2)

            })

        resources.sort(
            key=lambda x: x["priority_score"],
            reverse=True
        )

        return resources