import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from tmc.geometry_reader import GeometryReader

reader = GeometryReader()

csv = PROJECT_ROOT / \
"data/raw/TMC-2/Scene_02/geometry/calibrated/20251107/ch2_tmc_ncn_20251107T2205342105_g_grd_d18.csv"

df = reader.read(csv)

print("\nColumn Names\n")
print(df.columns.tolist())