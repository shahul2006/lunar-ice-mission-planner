from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT / "src"))

from data_processing.metadata_loader import MetadataLoader

loader = MetadataLoader()

xml = PROJECT_ROOT / "data/raw/OHRC/Scene_01/data/raw/20251105/ch2_ohr_nrp_20251105T1048273563_d_img_d18.xml"

meta = loader.load(xml)

print("\n========== METADATA ==========\n")

for key, value in meta.items():
    print(f"{key:25} : {value}")