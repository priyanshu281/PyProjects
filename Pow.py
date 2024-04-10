class Solution:
    def Pow(self, x:float, n:int)-> float:
        negflg=0
        if n==0 or x==1:
            return 1
        if n<0:
            negflg=True
            n=n*-1
        ans=1
        while n>0:
            if n%2==0:
                x=x*x
                n=n//2
            else:
                ans= ans*x
                n=n-1
        res= ans if not negflg else 1/ans
        return res

if __name__ == "__main__":
    s=Solution()
    res=s.Pow(2, -2)
    print(res)
