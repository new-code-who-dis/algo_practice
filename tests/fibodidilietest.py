import fibonaci.fibodidilie as fib
import unittest

class FiboTest(unittest.TestCase):
    def testFib1(self):
        self.assertEqual(fib.calcFib(1), 1)
    def testFib3(self):
        self.assertEqual(fib.calcFib(3), 2)
    def testFib10(self):
        self.assertEqual(fib.calcFib(10), 55)
    
    def testInd1(self):
        self.assertEqual(fib.calcIndex(1), 1)
    def testInd2(self):
        self.assertEqual(fib.calcIndex(2), 3)
    def testIndex55(self):
        self.assertEqual(fib.calcIndex(55), 10)
    def testIndex54(self):
        self.assertEqual(fib.calcIndex(54), "Next closest index is 10 which yields 55")
    def testLastDigitBasique(self):
        self.assertEqual(fib.calcLastDigitOfSum(3,9),6)
    def testLastDigitAgainBasique(self):
        self.assertEqual(fib.calcLastDigitOfSum(3,7),1)


if __name__ == '__main__':
    unittest.main()