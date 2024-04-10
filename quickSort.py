import array as arr
myarr=arr.array("i",[8,2,1,9,5])

li=[4,91,22,3,7,56,11,49]


def quickSort(mylist,l,r):
    if l<r:
        p=partitionIndex(mylist,l,r)
        quickSort(mylist,l,p-1)
        quickSort(mylist,p+1,r)
    else:
        return mylist


def partitionIndex(lis,l,r):
    piv=lis[r]
    i=l
    for j in range(l,r):
        if lis[j]<= piv:
            swap(lis,i,j)
            i=i+1
    swap(lis,i,r)
    return i


def swap(lis,i1,i2):
    tmp=lis[i1]
    lis[i1]=lis[i2]
    lis[i2]=tmp


if __name__=="__main__" :
    quickSort(li,0,len(li)-1)
    print(li)