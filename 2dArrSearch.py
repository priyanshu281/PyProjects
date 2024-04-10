class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        low = 0
        high = col * row - 1
        tmp = searchKey(matrix, target, low, high)
        if tmp > 0:
            return True
        else:
            return False

    def searchKey(matrix: List[List[int]], targ: int, l: int, h: int) -> int:
        if h >= l:
            mid = l + (h - l) / 2
            matrix_mid = matrix[mid / col][mid % col]
            if targ > matrix_mid:
                l = mid + 1
                return searchKey(matrix, targ, l, h)
            if targ < matrix_mid:
                h = mid - 1
                return searchKey(matrix, targ, l, h)
            if targ == matrix_mid:
                return mid
        else:
            return -1




