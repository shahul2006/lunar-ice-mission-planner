import xml.etree.ElementTree as ET
import numpy as np


class TMCReader:

    def __init__(self):
        pass

    def read(self, img_path, xml_path):

        root = ET.parse(xml_path).getroot()

        namespace = {
            "pds": "http://pds.nasa.gov/pds4/pds/v1"
        }

        array = root.find(".//pds:Array_2D_Image", namespace)

        data_type = array.find(
            ".//pds:data_type",
            namespace
        ).text

        axes = array.findall(
            ".//pds:Axis_Array",
            namespace
        )

        rows = int(
            axes[0].find("pds:elements", namespace).text
        )

        cols = int(
            axes[1].find("pds:elements", namespace).text
        )

        dtype_map = {
            "UnsignedByte": np.uint8,
            "UnsignedLSB2": np.uint16
        }

        dtype = dtype_map[data_type]

        image = np.fromfile(
            img_path,
            dtype=dtype
        )

        image = image.reshape(rows, cols)

        print("\n==============================")
        print("TMC IMAGE LOADED")
        print("==============================")
        print("Shape :", image.shape)
        print("Type  :", image.dtype)

        return image