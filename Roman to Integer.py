import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = 0
        self.assertEqual(Solution().romanToInt(Input),Output)
    def testSample(self):
        Input = "DCXXI"
        Output = 621
        self.assertEqual(Solution().romanToInt(Input),Output)

class Solution():
    def romanToInt(self, s):
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M":1000}
        if s == "":
            return 0
        ans = 0
        for item in s:
            ans += dic[item]
        return ans

if __name__ == '__main__':
    unittest.main()
