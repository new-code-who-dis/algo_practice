import fibodidilie
import unittest

class FiboTest(unittest.TestCase):
    def testFib1(self):
        self.assertEqual(fibodidilie.calcFib(1), 1)
    def testFib3(self):
        self.assertEqual(fibodidilie.calcFib(3), 2)
    def testFib10(self):
        self.assertEqual(fibodidilie.calcFib(10), 55)
    def testInd1(self):
        self.assertEqual(fibodidilie.calcIndex(1), 1)
    def testInd2(self):
        self.assertEqual(fibodidilie.calcIndex(2), 3)
    def testIndex55(self):
        self.assertEqual(fibodidilie.calcIndex(55), 10)
    def testIndex54(self):
        self.assertEqual(fibodidilie.calcIndex(54), 1234)


if __name__ == '__main__':
    unittest.main()