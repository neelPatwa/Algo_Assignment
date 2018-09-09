def get(arr): 
    n = len(arr) 
  
   
    lis = [1]*n 
  
    
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    
    maximum = 0
  
    
  
    return max(lis)


print("Enter Elemnets:")
arr = list(map(int,raw_input().split(" ")))
print ("Length of lis is "+str( get(arr)) )
