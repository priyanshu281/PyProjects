class Solution:
    maxLen = 0

    def checkMaxPalindrome(self, s, n, i, j):
        global maxLen
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        if maxLen < j - i - 1:
            Solution.lo = i + 1
            maxLen = j - i - 1

    def longestPalindrome(self, s: str) -> str:
        #global maxLen
        n = len(s)

        if n < 2:
            return s
        for i in range(n):
            self.checkMaxPalindrome(s, n, i, i)
            self.checkMaxPalindrome(s, n, i, i + 1)
        return s[Solution.lo: Solution.lo+Solution.maxLen]

if __name__=="__main__":
    s=Solution()
    res=s.longestPalindrome("babad")
    print(res)