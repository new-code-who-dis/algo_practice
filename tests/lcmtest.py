import lcm.lcm as lcm
import unittest

class LCMTest(unittest.TestCase):
    def testGCDLarge(self):
        self.assertEqual(lcm.calc_lcm(30,25),150)

if __name__ == '__main__':
    unittest.main()
