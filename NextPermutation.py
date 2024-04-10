from typing import List, Optional
class solution:
    def getNextPermutation(self, nums: List[int]) -> Optional[List[int]]:
        n = len(nums)
        pivot = -1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
        if pivot == -1:
            return nums.sort()
        new_pivot = -1
        for i in range(pivot + 1, n):
            if nums[pivot] < nums[i]:
                new_pivot = i

        nums[pivot], nums[new_pivot] = nums[new_pivot], nums[pivot]
        l = pivot + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        nums2=nums[:]
        return nums2
if __name__ ==  "__main__":
    li= [5,3,4,8,7,6]
    s= solution()
    print("li before:",li)
    res=s.getNextPermutation(li)
    print(li) #in place
    print(res)