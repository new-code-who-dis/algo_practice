import array_searches.array_searches as search
import unittest

class Array_Search_Test(unittest.TestCase):
    def testBinarySearchNumbers(self):
        self.assertEqual(search.binary_search([1,4,7,9,10,112,124],10),4)
    def testBinarySearchNotThere(self):
        self.assertEqual(search.binary_search([1,4,7,9,10,112,124],2),"NOT_FOUND")
    def testBinarySearchLast(self):
        self.assertEqual(search.binary_search([1,2,3,4,5,6,7,8,9,10],10),9)

if __name__ == '__main__':
    unittest.main()
# ok if all of the damn tests need this bs why dont i just have them all ref one thing
# ACTUALLY look up why this shit is here anyway