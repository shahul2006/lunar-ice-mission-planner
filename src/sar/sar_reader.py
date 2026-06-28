import xml.etree.ElementTree as ET
import numpy as np


class SARReader:

    def __init__(self):
        pass

    def read(self, dat_path, xml_path):

        root = ET.parse(xml_path).getroot()

        ns = {
            "pds": "http://pds.nasa.gov/pds4/pds/v1"
        }

        array = root.find(".//pds:Array_2D_Image", ns)

        data_type = array.find(
            ".//pds:data_type",
            ns
        ).text

        axes = array.findall(
            ".//pds:Axis_Array",
            ns
        )

        rows = int(
            axes[0].find("pds:elements", ns).text
        )

        cols = int(
            axes[1].find("pds:elements", ns).text
        )

        dtype_map = {
            "SignedByte": np.int8,
            "UnsignedByte": np.uint8,
            "UnsignedLSB2": np.uint16
        }

        dtype = dtype_map[data_type]

        print("\n==============================")
        print("SAR METADATA")
        print("==============================")
        print("Rows :", rows)
        print("Cols :", cols)
        print("Type :", data_type)

        data = np.memmap(
            dat_path,
            dtype=dtype,
            mode="r",
            shape=(rows, cols)
        )

        return data