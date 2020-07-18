import greedy_algunos.iwant7figures as chaching
import unittest

class MuneyTest(unittest.TestCase):
    def testLowBall(self):
        self.assertEqual(chaching.arrange_dat_coin(1234567), 7654321)
    def testNigthmare(self):
        self.assertEqual(chaching.thinkBroke([4,3,2,1]), [1,2,3,4])
    def testPoBrokeNFab(self):
        self.assertEqual(chaching.thinkBroke([0,0,0,0,1]), [0,0,0,0,1])
    def testAgeDisOrderedList(self):
        self.assertEqual(chaching.ageDiscrimination([1,5,6,6,10,12,13]),[[1],[5,6,6],[10,12],[13]])