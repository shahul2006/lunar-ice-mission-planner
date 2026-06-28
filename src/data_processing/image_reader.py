from pathlib import Path
import rasterio

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data" / "raw"


def read_images(extension):
    files = list(DATA_DIR.rglob(f"*{extension}"))

    print(f"\nFound {len(files)} {extension} files\n")

    for file in files:
        print("=" * 70)
        print(file.relative_to(PROJECT_ROOT))

        try:
            with rasterio.open(file) as src:
                print(f"Width      : {src.width}")
                print(f"Height     : {src.height}")
                print(f"Bands      : {src.count}")
                print(f"Data Type  : {src.dtypes}")
                print(f"CRS        : {src.crs}")
        except Exception as e:
            print("Cannot read:", e)


if __name__ == "__main__":
    read_images(".img")