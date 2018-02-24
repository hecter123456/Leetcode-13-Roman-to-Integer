import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = 0
        self.assertEqual(Solution().romanToInt(Input),Output)

class Solution():
    def romanToInt(self, s):
        if s == "":
            return 0

if __name__ == '__main__':
    unittest.main()
