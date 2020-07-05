import gcd.gcdish
import unittest

class GCDTest(unittest.TestCase):
    def testGCDSmall(self):
        # i dont get why it can't find the relative path, i doubt there are any functions in unittest called calc_gcd
        self.assertEqual(gcd.gcdish.calc_gcd(4,8), 4)
    def testGCDLarge(self):
        # i dont get why it can't find the relative path, i doubt there are any functions in unittest called calc_gcd
        self.assertEqual(gcd.gcdish.calc_gcd(3918848,1653264), 61232)

if __name__ == '__main__':
    unittest.main()
    