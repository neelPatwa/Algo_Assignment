def minSum(a):
    
    
    sum1=99999999
    for i in range(0,len(a)):
        
        for j in range(i,len(a)+1):
            
            l1=a[i:j+1]
	    
            t= sum(l1)
            if t<sum1:
                sum1=t
        
                
            
            #list.append(l1)
    
    return sum1

A=map(int,raw_input().split(' '))
print('Min Sum:'+str(minSum(A)))
