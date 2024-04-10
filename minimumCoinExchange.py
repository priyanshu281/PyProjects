#Using dynamic programming we have to get minimum number of coins whose total amount should be equal to the key



coins = [1, 5, 6 ,9]
coinsDenomDict = dict({1: [1], 2: [2]})
#coins.sort(reverse=True)
print(coins)
i = 0




 #while i < len(coins)-1:
def getDenominationsV1(amount,tmpL):
      """Using coin array in decending order and subtracting every coin's multiple from the key if there is remainder then repeating the process with remainder"""
      if amount in coinsDenomDict.keys():
            #print("amt",amount)
            #print("array",tmpL)
            tmpL= tmpL + coinsDenomDict.get(amount)
            print("Merged array",tmpL)
            return tmpL
      else:
            global i
            tmpL = tmpL + [coins[i]]*int(amount/coins[i])
            amount=amount % coins[i]
            #print("curr Amt ",amount)
            #print(tmpL)
            i=i+1
            getDenominationsV1(amount,tmpL)


def getDenominationsV2(key):
    """ Using DP with 2dArray"""
    ar2d=[[0]*key+1]*len(coins)

    for i in range(1,len(coins)-1):
        ar2d[i][0]=0
        for j in range(key):
            ar2d[0][j]=j
            if coins[i] > j:
                ar2d[i][j]=ar2d[i-1][j]
            else:
                ar2d[i][j] = min(ar2d[i-1][j],1+ar2d[i][j-coins[i]])

    return ar2d[len(coins)-1][key]

if __name__ == "__main__":
    key=11
    print(coinsDenomDict.keys())
    getDenominationsV2()
    li=getDenominationsV2(key)
    print(li)


""" Wrong approach with getDenominationsV1 as this is not dynamic programming rather more of a greedy algorithm
 also return statement has some bug """

