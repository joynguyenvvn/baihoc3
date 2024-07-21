
import unittest
import pandas as pd

from medical_data_visualizer import draw_cat_plot, draw_heat_map

class UnitTests(unittest.TestCase):
    def test_cat_plot(self):
        fig = draw_cat_plot()
        self.assertEqual(len(fig.axes), 2, "Number of axes should be 2")

    def test_heat_map(self):
        fig = draw_heat_map()
        self.assertEqual(len(fig.axes), 1, "Number of axes should be 1")

if __name__ == "__main__":
    unittest.main()
