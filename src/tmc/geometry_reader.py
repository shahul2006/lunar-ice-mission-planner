import pandas as pd


class GeometryReader:

    def read(self, csv_path):

        df = pd.read_csv(csv_path)

        print("\n==============================")
        print("TMC GEOMETRY LOADED")
        print("==============================")
        print("Rows    :", len(df))
        print("Columns :", len(df.columns))
        print()

        print(df.head())

        return df