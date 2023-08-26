import pandas as pd

class Concentration:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.mean = self.df.mean()
        self.dev = self.df.std()
        self.sum = self.df.sum()
        self.image = self.create_image()

    # might need to save image to a file, will explore later.
    @staticmethod
    def create_image():
        return None
        # do image stuff, maybe matplotlib
