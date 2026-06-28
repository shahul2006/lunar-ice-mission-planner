import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from reporting.mission_report import MissionReport

metadata = {
    "title": "Chandrayaan-2 OHRC Mission",
    "imaging_orbit_number": 27656
}

report = MissionReport().generate(

    metadata=metadata,

    landing_site=(953,631),

    path_length=1516,

    crater_count=4,

    ice_pixels=100264
)

print(report)