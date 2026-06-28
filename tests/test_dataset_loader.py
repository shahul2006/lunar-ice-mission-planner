from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.dataset_loader import DatasetLoader

loader = DatasetLoader(PROJECT_ROOT)

loader.summary()

print("\n")

scene = loader.get_scene("OHRC", "Scene_01")

print(scene)