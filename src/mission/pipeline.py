class MissionPipeline:

    def __init__(self):

        self.results = {}

    def add(self, key, value):
        self.results[key] = value

    def summary(self):

        print("\n===================================")
        print("MISSION PIPELINE SUMMARY")
        print("===================================")

        for key, value in self.results.items():

            print(f"{key:25}: {value}")

        print("===================================")

        return self.results