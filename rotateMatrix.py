from typing import List
class solution:
    def rotateMatrix(self, matrix: List[List[int]]):
        mt = list(zip(*matrix))
        matrix[:] = list(map(lambda x: x[::-1], mt))
        print(matrix)

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s= solution()
    s.rotateMatrix(matrix)
