import polynomial.poly as poly
import unittest

class PolyTest(unittest.TestCase):
    def testPolyNiave(self):
        self.assertEqual(poly.mult_poly([2,3,4],[3,4,5]),[6, 17, 34, 31, 20])
    def testPolyNiaveVariableLengthNiave(self):
        self.assertEqual(poly.mult_poly([1,2],[1,2,3]),[1, 4, 7, 6])
    def testPolyNiaveOddPair(self):
        self.assertEqual(poly.mult_poly([1,2,3,4],[4,3,2,1]),[4, 11, 20, 30, 20, 11, 4])
    def testPolyKaratsuba(self):
        self.assertEqual(poly.mult_karatsuba_style([1,2,3,4],[4,3,2,1]),[4, 11, 20, 30, 20, 11, 4])

if __name__ == '__main__':
    unittest.main()