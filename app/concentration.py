import pandas as pd

class Concentration:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.mean = str(self.df['concentration'].mean())
        self.dev = str(self.df['concentration'].std())
        self.sum = str(self.df['concentration'].sum())
        self.image = self.create_image()

    # might need to save image to a file, will explore later.
    @staticmethod
    def create_image():
        return None
        # do image stuff, maybe matplotlib
