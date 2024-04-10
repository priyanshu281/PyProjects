#https://leetcode.com/problems/majority-element/description/

from typing import List
class Solution:
    def majorityElementNby2(self, nums:List[int])-> int:
        n0= -99999
        cnt=0
        for i in range(len(nums)):
            if nums[i] ==n0:
                cnt +=1
            elif nums[i] != n0 and cnt==0:
                cnt=1
                n0=nums[i]
            else:
                cnt -=1

        return n0



