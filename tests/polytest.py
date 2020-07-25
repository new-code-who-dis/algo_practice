import polynomial.poly as poly
import unittest

class PolyTest(unittest.TestCase):
    def testPolyNiave(self):
        self.assertEqual(poly.mult_poly([2,3,4],[3,4,5]),{4:20,3:31,2:34,1:17,0:6})
    def testPolyNiaveVariableLength(self):
        self.assertEqual(poly.mult_poly([1,2],[1,2,3]),{3:6,2:7,1:4,0:1})

if __name__ == '__main__':
    unittest.main()