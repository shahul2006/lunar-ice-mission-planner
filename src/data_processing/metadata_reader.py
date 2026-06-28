from pathlib import Path
import xml.etree.ElementTree as ET


class MetadataReader:

    def __init__(self, project_root):

        self.project_root = Path(project_root)

        self.raw_dir = self.project_root / "data" / "raw"

    def scan_xml_files(self):

        xml_files = sorted(self.raw_dir.rglob("*.xml"))

        print("=" * 80)
        print(f"Found {len(xml_files)} XML files")
        print("=" * 80)

        for xml_file in xml_files:

            print("\n", xml_file.relative_to(self.project_root))

            self.read_xml(xml_file)

    def read_xml(self, xml_path):

        try:

            tree = ET.parse(xml_path)

            root = tree.getroot()

            print("Root Tag :", root.tag)

            print("Children :", len(root))

        except Exception as e:

            print("Error :", e)


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parents[2]

    reader = MetadataReader(project_root)

    reader.scan_xml_files()