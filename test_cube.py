import unittest
import cube

class TestCase(unittest.TestCase):
    def test_vol1(self):
        self.assertEqual(cube.calcVol(2,2,2), 8)
    def test_vol2(self):
        self.assertEqual(cube.calcVol(-2,2,2), 8)
    def test_vol3(self):
        self.assertEqual(cube.calcVol(2.3,2.8,2.1), 13.524)


if __name__ == '__main__':
    unittest.main()