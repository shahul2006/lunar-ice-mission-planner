import math


class CraterClassifier:

    def classify(self, candidates):

        results = []

        for x, y, r, circularity in candidates:

            area = math.pi * r * r

            if r < 8:
                size = "Small"
            elif r < 20:
                size = "Medium"
            else:
                size = "Large"

            confidence = circularity * 100

            results.append({
                "center": (x, y),
                "radius": r,
                "area": area,
                "size": size,
                "confidence": round(confidence, 2)
            })

        return results