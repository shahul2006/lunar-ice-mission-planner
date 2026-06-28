class MissionPlanner:

    def recommend(
        self,
        landing_sites,
        resources,
        rover_path_length,
        ice_volume
    ):

        best_landing = landing_sites[0] if landing_sites else None
        best_resource = resources[0] if resources else None

        mission_score = 0

        if best_resource:
            mission_score += best_resource["priority_score"] * 0.6

        if ice_volume:
            mission_score += (
                ice_volume["estimated_volume_m3"] / 1000
            ) * 0.4

        status = (
            "Recommended"
            if mission_score > 100
            else "Review Required"
        )

        return {
            "landing_site": best_landing,
            "resource": best_resource,
            "rover_path_length": rover_path_length,
            "estimated_volume": ice_volume,
            "mission_score": round(mission_score, 2),
            "status": status,
        }