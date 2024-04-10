from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i == 0 or (nums[i] != nums[i - 1]):
                k = n - 1
                j = i + 1
            while j < k:
                if nums[i] + nums[k] + nums[j] == 0:
                    res += [[nums[i], nums[j], nums[k]]]
                    while (j < k and nums[j] == nums[j + 1]):
                        j = j + 1
                    while (j < k and nums[k] == nums[k - 1]):
                        k = k - 1
                    j = j + 1
                    k = k - 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    j = j + 1
                else:
                    k = k - 1
        return res



if __name__=="__main__":
    s= Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))