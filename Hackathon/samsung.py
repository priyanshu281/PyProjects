
def compare(arr1, arr2):
    n= len(arr1)
    m= len(arr2)

    #i=j=0
    d1={}
    d2={}
    for i in arr1:
        if i not in d1:
            d1[i]=1  # 2 -> 1
        else:
            d1[i] +=1 # 2 -> 2
    for j in arr2:
        if j not in d2:
            d2[j] =1
        else:
            d2[j] +=1

    for k in d1:
        if k in d2:
            if d1[k] == d2[k]:
                continue

            else:
                return False
        else:
            return False
    return True
    #if d1 == d2:
    #    return True
    #else:
    #    return False


    #for i in range(n):
     #   if arr1[i]== arr2[j]:
           # j +=1
    #    else:
    #        return False
    #return True


arr1= [1, 1, 2, 4]
arr2= [1, 1, 2, 4]

b=compare(arr1, arr2)
print(b)