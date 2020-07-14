import greedy_algunos.iwant7figures as chaching
import unittest

class MuneyTest(unittest.TestCase):
    def testLowBall(self):
        self.assertEqual(chaching.arrange_dat_coin(1234567), 7654321)