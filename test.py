import unittest
from perfectsquare import isPerfectSquare
class TestisPerfectSquare(unittest.TestCase):
    
    def test_case3(self):
        result = isPerfectSquare(10)
        self.assertEqual(result,False)
    def test_case4(self):
        result = isPerfectSquare(8)
        self.assertEqual(result,False)
    def test_case5(self):
        result = isPerfectSquare(9)
        self.assertEqual(result,True)
        
    # wrong testcase
    def test_case1(self):
        result = isPerfectSquare(16)
        self.assertEqual(result,False)
    # wrong testcase
    def test_case2(self):
        result = isPerfectSquare(3)
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()
