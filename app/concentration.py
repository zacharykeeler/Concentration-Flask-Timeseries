import pandas as pd
import matplotlib.pyplot as plt

class Concentration:
    _img_location = '3D_concentration_visualization.png'

    def __init__(self, csv_file):
        self._df = pd.read_csv(csv_file)
        self._check_required_columns()
        self._create_image()

    @property
    def img_location(self):
        return self._img_location

    def mean(self):
        return str(self._df['concentration'].mean())

    def std_dev(self):
        return str(self._df['concentration'].std())

    def sum(self):
        return str(self._df['concentration'].sum())

    def _check_required_columns(self):
        required_columns = ['z', 'y', 'x', 'concentration']
        missing_columns = [col for col in required_columns if col not in self._df.columns]
        
        if missing_columns:
            raise Exception(f"Missing columns in the CSV file: {', '.join(missing_columns)}")

    def _create_image(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        scatter = ax.scatter(self._df['x'], self._df['y'], self._df['z'], c=self._df['concentration'], cmap='coolwarm')

        cbar = fig.colorbar(scatter, ax=ax)
        cbar.set_label('Concentration')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('3D Visualization of Concentration')

        plt.savefig(self._img_location, dpi=300)
