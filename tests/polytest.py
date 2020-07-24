import polynomial.poly as poly
import unittest

class PolyTest(unittest.TestCase):
    def testPolyNiave(self):
        self.assertEqual(poly.mult_poly([2,3,4],[3,4,5]),{4:20,3:31,2:34,1:17,0:6})

if __name__ == '__main__':
    unittest.main()