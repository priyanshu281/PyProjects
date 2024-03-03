arr= [1, 2, 2]
n= len(arr)
res=[[arr[0]]]
for i in range(n):
    tmp = []
    for j in range(i,n):
        tmp.append(arr[j])
    res.append(tmp)

print(res)