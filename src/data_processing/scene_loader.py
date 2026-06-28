from pathlib import Path

from data_processing.dataset_loader import DatasetLoader
from data_processing.metadata_loader import MetadataLoader


class SceneLoader:

    def __init__(self, project_root):

        self.project_root = Path(project_root)

        self.dataset_loader = DatasetLoader(project_root)
        self.metadata_loader = MetadataLoader()

    def load(self, dataset_name, scene_name):

        scene = self.dataset_loader.get_scene(dataset_name, scene_name)

        result = {
            "dataset": dataset_name,
            "scene": scene_name,
            "metadata": [],
            "files": scene
        }

        # Read all XML metadata
        for group in scene.values():

            for file in group:

                if file.is_file() and file.suffix.lower() == ".xml":

                    try:
                        meta = self.metadata_loader.load(file)

                        result["metadata"].append(meta)

                    except Exception as e:

                        print(f"Could not read {file.name}: {e}")

        return result