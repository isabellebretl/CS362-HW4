import unittest
import avg

class TestCase(unittest.TestCase):
    def test_avg1(self):
        self.assertEqual(avg.calcAvg([1,2,3,4,5]), 3)
    def test_avg2(self):
        self.assertEqual(avg.calcAvg([]), 0)
    def test_avg3(self):
        self.assertEqual(avg.calcAvg([-4.4,-5.5,-6.6]), -5.5)


if __name__ == '__main__':
    unittest.main()