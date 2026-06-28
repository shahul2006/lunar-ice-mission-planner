import cv2


class CraterCandidates:

    def __init__(self):
        pass

    def extract(self, edges):

        contours, _ = cv2.findContours(
            edges,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        candidates = []

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area < 40:
                continue

            perimeter = cv2.arcLength(cnt, True)

            if perimeter == 0:
                continue

            circularity = 4 * 3.14159 * area / (perimeter * perimeter)

            if circularity < 0.45:
                continue

            (x, y), radius = cv2.minEnclosingCircle(cnt)

            candidates.append(
                (
                    int(x),
                    int(y),
                    int(radius),
                    circularity
                )
            )

        return candidates