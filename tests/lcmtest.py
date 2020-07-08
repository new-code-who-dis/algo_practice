import lcm.lcm as lcm
import unittest

class LCMTest(unittest.TestCase):
    def testLCMSmall(self):
        self.assertEqual(lcm.calc_lcm(30,25),150)
    def testLCDSmall(self):
        self.assertEqual(lcm.calc_lcd(30,25),5)
    def testLCDMultipleDivisors(self):
        self.assertEqual(lcm.calc_lcd(50,20),2)

#refactor test structure so theres not so much going on, like they all take 2 inputs and 1 expected
# theres probably a nice clean way to make it look purdy, unncessary but purdy
if __name__ == '__main__':
    unittest.main()
