class Solution:
    def NtoSay(self, num:int):
        i = j = 0
        ns = str(num)
        curr = ""
        n=len(ns)
        while i < n:
            count = 0

            while j < n and ns[i] == ns[j]:
                j += 1
                count += 1
            curr += str(count) + ns[i]
            i = j
        return curr

    def CountNsay(self, n: int):
        if n == 1:
            return "1"
        nMinus1 = self.CountNsay(n-1)
        tmp = int(nMinus1)
        return self.NtoSay(tmp)


if __name__ == "__main__":
    s=Solution()
    print(s.CountNsay(7))


