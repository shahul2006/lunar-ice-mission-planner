import matplotlib.pyplot as plt


class MissionDashboard:

    def show(
        self,
        original,
        roughness,
        ice,
        landing,
        hazard,
        rover
    ):

        plt.figure(figsize=(18, 10))

        plt.subplot(231)
        plt.imshow(original, cmap="gray")
        plt.title("OHRC Image")
        plt.axis("off")

        plt.subplot(232)
        plt.imshow(roughness, cmap="hot")
        plt.title("Terrain Roughness")
        plt.axis("off")

        plt.subplot(233)
        plt.imshow(ice, cmap="Blues")
        plt.title("Ice Probability")
        plt.axis("off")

        plt.subplot(234)
        plt.imshow(landing, cmap="Greens")
        plt.title("Landing Suitability")
        plt.axis("off")

        plt.subplot(235)
        plt.imshow(hazard)
        plt.title("Hazard Map")
        plt.axis("off")

        plt.subplot(236)
        plt.imshow(rover)
        plt.title("Rover Path")
        plt.axis("off")

        plt.suptitle(
            "CHANDRAYAAN-2 LUNAR MISSION PLANNER",
            fontsize=18,
            fontweight="bold"
        )

        plt.tight_layout()

        plt.show()