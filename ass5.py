def check(A,sum):
     
   
    A.sort()
    arr_size=len(A)
    l = 0
    r = arr_size-1
     
    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0

print("Enter Array")

A = list(map(int ,raw_input().split(" ")))
print("Enter Sum Value")
n = int(input())
if (check(A,n)):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")
