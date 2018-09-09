import sys
def smallestSumSubarr(arr, n):
   
    min_ending_here = sys.maxint
     
   
    min_so_far = sys.maxint
     
    
    for i in range(n):
       
        if (min_ending_here > 0):
            min_ending_here = arr[i]
         
   
        else:
            min_ending_here += arr[i]
          
       
        min_so_far = min(min_so_far, min_ending_here)
     
    
    return min_so_far

print("Enter Elements:")
arr = map(int,raw_input().split(' '))
n = len(arr)
print "Smallest sum: ", smallestSumSubarr(arr, n)
