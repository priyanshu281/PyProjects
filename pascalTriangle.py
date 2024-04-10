class Solution:
    def pascalTriangleSampleTest(self):
        a=[1]
        res=[]
        t=[(map(lambda x,y : x+y, a+[0], [0] + a))]
        print(t)



if __name__== "__main__":
    s=Solution()
    s.pascalTriangleSampleTest()