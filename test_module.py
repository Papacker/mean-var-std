import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):
    def test_valid_input(self):
        sample = [0,1,2,3,4,5,6,7,8]
        expected = {
            'mean': [[3.0, 4.0, 5.0],
                     [1.0, 4.0, 7.0],
                     4.0],
            'variance': [[6.0, 6.0, 6.0],
                         [0.6666666666666666]*3,
                         6.666666666666667],
            'standard deviation': [[2.449489742783178]*3,
                                   [0.816496580927726]*3,
                                   2.581988897471611],
            'max': [[6,7,8],[2,5,8],8],
            'min': [[0,1,2],[0,3,6],0],
            'sum': [[9,12,15],[3,12,21],36]
        }
        result = calculate(sample)
        self.assertEqual(result, expected)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            calculate([1,2,3,4,5])  # liian lyhyt lista

if __name__ == '__main__':
    unittest.main()
