from datetime import datetime


class MissionReport:

    def generate(
        self,
        metadata,
        landing_site,
        path_length,
        crater_count,
        ice_pixels
    ):

        report = f"""
============================================================
        CHANDRAYAAN-2 LUNAR MISSION REPORT
============================================================

Generated:
{datetime.now()}

------------------------------------------------------------

MISSION INFORMATION

Mission :
{metadata.get("title","Unknown")}

Orbit :
{metadata.get("imaging_orbit_number","Unknown")}

------------------------------------------------------------

LANDING

Landing Site :
{landing_site}

------------------------------------------------------------

ICE ANALYSIS

Detected Ice Pixels :
{ice_pixels}

------------------------------------------------------------

CRATER ANALYSIS

Detected Craters :
{crater_count}

------------------------------------------------------------

ROVER

Path Length :
{path_length}

------------------------------------------------------------

MISSION STATUS

SUCCESS

============================================================
"""

        return report