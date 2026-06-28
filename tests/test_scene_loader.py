from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.scene_loader import SceneLoader

loader = SceneLoader(PROJECT_ROOT)

scene = loader.load("OHRC", "Scene_01")

print("=" * 60)
print("DATASET :", scene["dataset"])
print("SCENE   :", scene["scene"])
print("=" * 60)

print("\nMetadata files loaded :", len(scene["metadata"]))

for i, meta in enumerate(scene["metadata"], start=1):
    print(f"\nMetadata #{i}")
    print("Title :", meta.get("title"))
    print("File  :", meta.get("file_name"))
    print("Orbit :", meta.get("imaging_orbit_number"))