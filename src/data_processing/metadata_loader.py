from pathlib import Path
import xml.etree.ElementTree as ET


class MetadataLoader:

    def __init__(self):
        self.ns = {
            "pds": "http://pds.nasa.gov/pds4/pds/v1",
            "isda": "https://isda.issdc.gov.in/pds4/isda/v1"
        }

    def load(self, xml_path):

        xml_path = Path(xml_path)

        tree = ET.parse(xml_path)
        root = tree.getroot()

        metadata = {}

        # ---------- Identification ----------

        metadata["title"] = self.find(root, ".//pds:title")
        metadata["logical_identifier"] = self.find(root, ".//pds:logical_identifier")
        metadata["start_time"] = self.find(root, ".//pds:start_date_time")
        metadata["stop_time"] = self.find(root, ".//pds:stop_date_time")

        # ---------- File ----------

        metadata["file_name"] = self.find(root, ".//pds:file_name")
        metadata["file_size"] = self.find(root, ".//pds:file_size")

        # ---------- Image ----------

        metadata["data_type"] = self.find(root, ".//pds:data_type")

        axes = root.findall(".//pds:Axis_Array", self.ns)

        for axis in axes:

            axis_name = axis.find("pds:axis_name", self.ns).text
            elements = axis.find("pds:elements", self.ns).text

            metadata[axis_name] = int(elements)

        # ---------- Product Parameters ----------

        params = root.find(".//isda:Product_Parameters", self.ns)

        if params is not None:

            for child in params:

                tag = child.tag.split("}")[-1]

                if child.text:

                    metadata[tag] = child.text.strip()

        return metadata

    def find(self, root, xpath):

        node = root.find(xpath, self.ns)

        if node is None:
            return None

        return node.text