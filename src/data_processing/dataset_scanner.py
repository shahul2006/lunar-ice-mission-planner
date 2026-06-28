from pathlib import Path

print(" Script started...")

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
print(f"Project Root : {PROJECT_ROOT}")

# Raw data folder
DATA_DIR = PROJECT_ROOT / "data" / "raw"
print(f"Data Folder  : {DATA_DIR}")


DATASETS = {
    "SAR": DATA_DIR / "SAR",
    "OHRC": DATA_DIR / "OHRC",
    "TMC-2": DATA_DIR / "TMC-2"
}


def scan_dataset(dataset_name, dataset_path):
    print(f"\n{'='*60}")
    print(f"{dataset_name} DATASET")
    print(f"{'='*60}")

    if not dataset_path.exists():
        print(f"Folder not found: {dataset_path}")
        return

    scenes = sorted(dataset_path.iterdir())

    if len(scenes) == 0:
        print("No scenes found.")
        return

    for scene in scenes:
        if scene.is_dir():
            print(f"\nScene : {scene.name}")

            file_count = 0

            for file in scene.rglob("*"):
                if file.is_file():
                    file_count += 1
                    print("   ", file.relative_to(scene))

            print(f"Total Files : {file_count}")


def main():

    print("\n")
    print("=" * 70)
    print("CHANDRAYAAN-2 DATASET SCANNER")
    print("=" * 70)

    for name, path in DATASETS.items():
        scan_dataset(name, path)

    print("\n")
    print("=" * 70)
    print("Scan Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()