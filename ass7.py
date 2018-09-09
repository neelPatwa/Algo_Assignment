def compare(arr,p,mid,q,res):
    c = 0
    for i in range(mid+1,q):
        if res[i] == 1:
            c = i
            break
    for i in range(p,mid+1):
        if res[i] == 1:
            if arr[i][1] <= arr[c][1]:
                res[i] = 0

def nonDom(arr,p,q,res):
    mid = 0
   
    if p == q:
        res[p] = 1

    elif p+1 == q:
        if (arr[p][0] <= arr[q][0]) and (arr[p][1] <= arr[q][1]):
            res[q] = 1
            res[p] = 0
        elif (arr[p][0] >= arr[q][0]) and (arr[p][1] >= arr[q][1]):
            res[q] = 0
            res[p] = 1
        else:
            res[q] = 1
            res[p] = 1

    else:
        mid = (p+q)/2
       
        nonDom(arr,p,mid,res)
        nonDom(arr,mid+1,q,res)
        compare(arr,p,mid,q,res)



points = [
    (9,31),(1,3),(12,12),(45,12),(19,41),(34,41),(6,132),(123,142),(25,112),(12,1)
]
result = [0]*len(points)
points.sort(key = lambda e : e[0])
print points
nonDom(points,0,len(points)-1,result)
for r in range(len(points)):
    if result[r] == 1:
        print points[r]
