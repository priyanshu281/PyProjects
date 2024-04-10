class solution:
    def countSubarrayXorBrutForce(self, arr, target):
        n=len(arr)
        cnt=0
        for i in range(n):
            for j in range(i,n):
                xor_sum=0
                for k in range(i,j+1):
                    print(arr[k])
                    xor_sum=xor_sum ^ arr[k]
                if xor_sum== target:
                    cnt +=1
                print("new sub-array ")
        return cnt

    def countSubarrayXorOptimal(self, arr, target):
        n=len(arr)
        cnt=0
        for i in range(n):
            xor_sum=0
            for j in range(i, n):
                xor_sum=arr[j] ^ xor_sum
                if xor_sum== target:
                    cnt+=1
        return cnt

    def countSubarrayXorBestTimeComplexity(self, arr, k):
        n=len(arr)
        cnt=0
        hm={0:1}
        xor_sum=0
        for i in range(n):
            xor_sum= xor_sum^arr[i]
            if xor_sum^k in hm:
                 cnt += hm[xor_sum^k]

            if xor_sum not in hm:
                hm[xor_sum] = 1
            else:
                hm[xor_sum] += 1
        return cnt






    def countSubarrayXor(self, arr, target):
        n=len(arr)
        cnt=0
        for i in range(n):
            for j in range(i,n):
                xor_sum=0
                for k in range(i,j+1):
                    print(arr[k])
                    xor_sum=xor_sum ^ arr[k]
                if xor_sum== target:
                    cnt +=1
                print("new sub-array ")
        return cnt




if __name__ =="__main__":
    s=solution()
    #res=s.countSubarrayXorBrutForce([4, 2, 2, 6, 4], 6)
    res1= s.countSubarrayXorOptimal([4,2,2,6,4],6)
    resUsingDict= s.countSubarrayXorBestTimeComplexity([4, 2, 2, 6, 4], 6)
    print("most optimal",resUsingDict)
    print("better",res1)



