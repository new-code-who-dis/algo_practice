import gcd.gcdish
import unittest

class GCDTest(unittest.TestCase):
    def testGCD(self):
        # i dont get why it can't find the relative path, i doubt there are any functions in unittest called calc_gcd
        self.assertEqual(gcd.gcdish.calc_gcd(4,8), 4)

if __name__ == '__main__':
    unittest.main()
    