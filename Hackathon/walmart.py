class Walmart:
    def main():
        matrix =[[2, 5, 1, 4], [3, 14,12, 77]]
        r_t = 0
        c_r = len(matrix[0])-1
        r_b = len(matrix)-1
        c_l = 0
        #print from top
        j=r_t
        for j in range(c_l, c_r):
            print(matrix[r_t][j])
        r_t +=1

    # print  right columns
    #i=r_t
        j=c_r
        for i in range(r_t,r_b):
            print(matrix[i][j])
        c_r -=1

    #print from bottom rows
        i= r_b
        for j in range(c_r, c_l):
            print(matrix[i][j])
        r_b -= 1


    #print from left cols
        j=c_l
        for i in range(r_b, r_t):
            print(matrix[i][j])
        c_l +=1

    if __name__ == "__main__":
        main()


