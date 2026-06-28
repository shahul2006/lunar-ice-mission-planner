from pathlib import Path
import numpy as np
import xml.etree.ElementTree as ET


class BinaryImageReader:

    TYPE_MAP = {
        "UnsignedByte": np.uint8,
        "SignedByte": np.int8,
        "UnsignedLSB2": np.dtype("<u2"),   # Little-endian unsigned 16-bit
        "SignedLSB2": np.dtype("<i2")
    }

    def read(self, image_path, xml_path):

        tree = ET.parse(xml_path)
        root = tree.getroot()

        namespace = {"pds": "http://pds.nasa.gov/pds4/pds/v1"}

        array = root.find(".//pds:Array_2D_Image", namespace)

        offset = int(array.find("pds:offset", namespace).text)

        dtype_name = array.find(
            "pds:Element_Array/pds:data_type",
            namespace
        ).text

        axes = array.findall("pds:Axis_Array", namespace)

        height = int(axes[0].find("pds:elements", namespace).text)
        width = int(axes[1].find("pds:elements", namespace).text)

        dtype = self.TYPE_MAP[dtype_name]

        image = np.memmap(
            image_path,
            dtype=dtype,
            mode="r",
            offset=offset,
            shape=(height, width)
        )

        print("=" * 70)
        print("Image Loaded Successfully")
        print("=" * 70)
        print("File      :", Path(image_path).name)
        print("Type      :", dtype_name)
        print("Shape     :", image.shape)
        print("Data Type :", image.dtype)

        return image


if __name__ == "__main__":

    print("BinaryImageReader created successfully.")