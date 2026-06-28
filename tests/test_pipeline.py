import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from mission.pipeline import MissionPipeline

pipeline = MissionPipeline()

pipeline.add("Mission", "Chandrayaan-2")
pipeline.add("Landing Site", (953, 631))
pipeline.add("Detected Craters", 4)
pipeline.add("Ice Pixels", 100264)
pipeline.add("Estimated Ice Volume (m3)", 8843.28)
pipeline.add("Rover Path Length", 1516)
pipeline.add("Mission Status", "Recommended")

pipeline.summary()