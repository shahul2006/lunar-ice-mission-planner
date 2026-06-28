from pathlib import Path


class DatasetLoader:

    def __init__(self, project_root):

        self.project_root = Path(project_root)

        self.raw_path = self.project_root / "data" / "raw"

        self.datasets = {}

        self.scan()

    def scan(self):

        for dataset in self.raw_path.iterdir():

            if not dataset.is_dir():
                continue

            dataset_name = dataset.name

            self.datasets[dataset_name] = {}

            for scene in sorted(dataset.glob("Scene_*")):

                scene_name = scene.name

                self.datasets[dataset_name][scene_name] = {

                    "browse": list(scene.glob("browse/**/*")),

                    "data": list(scene.glob("data/**/*")),

                    "geometry": list(scene.glob("geometry/**/*")),

                    "miscellaneous": list(scene.glob("miscellaneous/**/*"))

                }

    def summary(self):

        print("\n" + "=" * 60)
        print("CHANDRAYAAN-2 DATASET SUMMARY")
        print("=" * 60)

        for dataset, scenes in self.datasets.items():

            print(f"\n{dataset}")

            for scene, folders in scenes.items():

                total = 0

                print(f"  {scene}")

                for folder, files in folders.items():

                    count = len([f for f in files if f.is_file()])

                    total += count

                    print(f"      {folder:<15} {count}")

                print(f"      Total Files : {total}")

    def get_scene(self, dataset, scene):

        return self.datasets[dataset][scene]