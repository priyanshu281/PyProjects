# https://leetcode.com/problems/set-matrix-zeroes/description/
class solution:
    def setMatrixZero(self, matrix): # if using self then it means class has to be instantiate ,
        # if not using self then Solution.setMatrixZero
        cols= len(matrix[0])
        rows= len(matrix)
        col0= row0=0
        for i in range(rows):
            if matrix[i][0] == 0:
                col0=1
                break
        for j in range(cols):
            if matrix[0][j] ==0:
                row0=1
                break

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] ==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(rows-1,0,-1):
            for j in range(cols-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j] == 0:
                    matrix[i][j]=0

        for i in range(rows):
            if col0==1:
                matrix[i][0]=0
        for j in range(cols):
            if row0 ==1:
                matrix[0][j] =0

if __name__ == "__main__":
    matrix1=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s = solution()
    a= list(zip(*matrix1))
    
    print(a)
    s.setMatrixZero(matrix1)
    print(matrix1)




