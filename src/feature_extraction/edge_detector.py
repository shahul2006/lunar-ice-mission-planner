import cv2


class EdgeDetector:

    def __init__(self):
        pass

    def canny(self, image):

        edges = cv2.Canny(
            image,
            threshold1=50,
            threshold2=150
        )

        return edges