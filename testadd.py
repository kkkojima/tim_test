import unittest
from add import add

class TestAdd(unittest.TestCase):

    def testadd(self):
        ret = add(1, 2)
        print("testadd is ", ret)
        self.assertEqual(3, ret)

    def testadd2(self):
        ret = add(5,5)
        print("testadd2 is ",ret)
        self.assertEqual(10, ret)

if __name__ == "__main__":
    unittest.main()