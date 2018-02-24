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
    def testMinusCase(self):
        Input = "MCMLIV"
        Output = 1954
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
        ans = 0
        last = 0
        for item in s:
            if last < dic[item]:
                ans -= last*2
            last = dic[item]
            ans += dic[item]
        return ans

if __name__ == '__main__':
    unittest.main()
