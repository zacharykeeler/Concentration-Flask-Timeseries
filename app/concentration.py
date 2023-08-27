import pandas as pd
import matplotlib.pyplot as plt

class Concentration:
    def __init__(self, csv_file):
        df = pd.read_csv(csv_file)
        self.mean = str(df['concentration'].mean())
        self.dev = str(df['concentration'].std())
        self.sum = str(df['concentration'].sum())
        self.image_location = '3D_concentration_visualization.png'
        self.create_image(df, self.image_location)

    @staticmethod
    def create_image(df, location):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        # 'c' determines the color based on the concentration value.
        # 'cmap' is the colormap used. Coolwarm is blue to red.
        # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        scatter = ax.scatter(df['x'], df['y'], df['z'], c=df['concentration'], cmap='coolwarm')

        cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
        cbar.set_label('Concentration')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('3D Visualization of Concentration')

        plt.savefig(location, dpi=300)
