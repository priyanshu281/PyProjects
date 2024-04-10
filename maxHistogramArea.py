from typing import List

def largestRectangleArea(
        heights: List[int]) -> int:
    stk = []
    n = len(heights)
    maxArea = 0
    for i in range(n + 1):
        if i == n:
            h = 0
        else:
            h = heights[i]

        if not stk or heights[stk[-1]] <= h:
            stk.append(i)
        else:
            tp = stk.pop()
            maxArea = max(maxArea, heights[tp] * (i if not stk else i - 1 - stk[-1]))
            i -= 1
    return maxArea

if __name__=="__main__" :
    res=largestRectangleArea([2,1,5,6,2,3])
    print(res)