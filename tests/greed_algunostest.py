import greedy_algunos.iwant7figures as chaching
import unittest

class MuneyTest(unittest.TestCase):
    def testLowBall(self):
        self.assertEqual(chaching.arrange_dat_coin(1234567), 7654321)
    def testNigthmare(self):
        self.assertEqual(chaching.thinkBroke([4,3,2,1]), [1,2,3,4])