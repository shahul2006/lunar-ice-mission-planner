from data_processing.image_reader import ImageReader
from sar.sar_reader import SARReader
from fusion.feature_fusion import FeatureFusion
from ice_detection.ice_candidate_detector import IceCandidateDetector
from landing_site.best_landing_site import BestLandingSite
from path_planning.rover_traverse import RoverTraverse
from reporting.mission_report import MissionReport


class MissionPlanner:

    def __init__(self):
        self.image_reader = ImageReader()
        self.sar_reader = SARReader()
        self.feature_fusion = FeatureFusion()
        self.ice_detector = IceCandidateDetector()
        self.landing_site = BestLandingSite()
        self.rover = RoverTraverse()
        self.report = MissionReport()

    def run(
        self,
        ohrc_image,
        sar_image,
        tmc_geometry=None
    ):
        """
        Main mission pipeline.
        """

        # ----------------------------
        # Feature Fusion
        # ----------------------------
        features = self.feature_fusion.combine(
            ohrc_image,
            sar_image
        )

        # ----------------------------
        # Ice Detection
        # ----------------------------
        ice_map = self.ice_detector.detect(features)

        # ----------------------------
        # Landing Site
        # ----------------------------
        landing = self.landing_site.find_best_site(
            ice_map
        )

        # ----------------------------
        # Rover Traverse
        # ----------------------------
        path = self.rover.plan(
            landing,
            ice_map
        )

        return {
            "landing_site": landing,
            "path": path,
            "ice_map": ice_map,
        }