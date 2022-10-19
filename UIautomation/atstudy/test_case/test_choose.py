import os
import unittest
import warnings
import sys
from UIautomation.atstudy.business.choose_bus import choose
from UIautomation.atstudy.test_data.testdata import get_csv_data
sys.path.append('..')


class TestChoose(unittest.TestCase):
    csv_file = os.path.abspath(os.path.dirname(os.getcwd()))+"/test_data/choose.csv"

    def setUp(self):
        print('Start test')
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        print('Finish test')

    def test_choose_01(self):
        print(self.csv_file)
        data = get_csv_data(self.csv_file, 1)
        self.assertTrue(choose(data[0], data[1], data[2]))

    def test_choose_02(self):
        print(self.csv_file)
        data = get_csv_data(self.csv_file, 2)
        self.assertTrue(choose(data[0], data[1], data[2]))

    def test_choose_03(self):
        print(self.csv_file)
        data = get_csv_data(self.csv_file, 3)
        self.assertTrue(choose(data[0], data[1], data[2]))

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
