import cv2
import numpy as np

from path_planning.astar import AStarPlanner


class RoverTraverse:

    def plan(
        self,
        landing_map,
        ice_mask,
        landing_site
    ):

        # --------------------------------------------------
        # Find the Largest Ice Region
        # --------------------------------------------------

        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
            ice_mask,
            connectivity=8
        )

        largest_area = 0
        goal = None

        for i in range(1, num_labels):

            area = stats[i, cv2.CC_STAT_AREA]

            if area > largest_area:

                largest_area = area

                cx, cy = centroids[i]

                goal = (int(cy), int(cx))

        if goal is None:
            raise Exception("No ice candidates found.")

        # --------------------------------------------------
        # Build Cost Map
        # --------------------------------------------------

        cost = 255 - landing_map

        planner = AStarPlanner()

        path = planner.search(
            cost.astype(np.float32),
            (landing_site[1], landing_site[0]),   # (row, col)
            goal
        )

        # --------------------------------------------------
        # Visualization
        # --------------------------------------------------

        display = cv2.cvtColor(
            landing_map,
            cv2.COLOR_GRAY2BGR
        )

        # Draw Rover Path
        for r, c in path:
            cv2.circle(display, (c, r), 1, (0, 0, 255), -1)

        # Draw Landing Site (Green)
        cv2.circle(
            display,
            landing_site,
            8,
            (0, 255, 0),
            -1
        )

        # Draw Ice Goal (Blue)
        cv2.circle(
            display,
            (goal[1], goal[0]),
            8,
            (255, 0, 0),
            -1
        )

        return display, path