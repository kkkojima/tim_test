from calctax import calc_tax
import unittest


class testCalcTax(unittest.TestCase):
    def test_calctax(self):
        #うまい棒 (税抜き15円)
        self.assertEqual(16, calc_tax(15, 0.1))
        
    def test_calctax(self):
        #イタリアン(税抜き80000円)
        self.assertEqual(88000, calc_tax(80000, 0.1))


if __name__ == "__main__":
    unittest.main()