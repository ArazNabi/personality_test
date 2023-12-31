import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class RadarChart:
    def __init__(self, data):
        self.categories = ['Feeling', 'Perceiving', 'Introversion', 'Sensing', 'Thinking', 'Judging', 'Extroversion', 'Intuition']
        self.data = data
        self.title = data['Name']

    def create_chart(self):
        num_categories = len(self.categories)
        angles = np.linspace(0,2 * np.pi, num_categories, endpoint=False).tolist()
        angles += angles[:1]

        fig = plt.figure(figsize=(5,5))
        ax = fig.add_subplot(111, polar=True)
        ax.set_thetagrids(np.degrees(angles[:-1]), labels=self.categories)

        self.data += [self.data[0]]

        ax.fill(angles, self.data, 'green', alpha=0.1)
        ax.plot(angles, data, 'o-', linewidth=2, color='green')  
        ax.set_rlabel_position(90)
        plt.title(self.title)
        plt.show()

# if __name__ == "__main__":
#     categories = ['Feeling', 'Perceiving', 'Introversion', 'Sensing', 'Thinking', 'Judging', 'Extroversion', 'Intuition']
#     data = [4, 3, 5, 2, 4, 3, 5, 2]  

#     radar_chart = RadarChart(data)
#     radar_chart.create_chart()




import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

dummy_test = pd.read_csv(CURR_DIR_PATH + '\\' +
    'dummy_test.csv',
    delimiter=',')

RadarChart(dummy_test)