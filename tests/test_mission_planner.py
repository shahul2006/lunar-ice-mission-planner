import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from mission.mission_planner import MissionPlanner

landing_sites = [
    {
        "x": 953,
        "y": 631,
        "score": 238
    }
]

resources = [
    {
        "priority_score": 7741.62,
        "center": (612, 511),
        "confidence": 91.7
    }
]

ice_volume = {
    "estimated_volume_m3": 8843.28
}

planner = MissionPlanner()

mission = planner.recommend(
    landing_sites,
    resources,
    rover_path_length=1516,
    ice_volume=ice_volume
)

print("\n==============================")
print("MISSION DECISION")
print("==============================")

for key, value in mission.items():
    print(f"{key}: {value}")