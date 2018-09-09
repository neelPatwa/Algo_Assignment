print ("ENTER  NUMBERS.")
a=list(map(int ,raw_input().split(" ")))
n=len(a)
k=max(a)

b=[0 for i in range(k+1)] 
c=[0 for i in range(n)] 

for i in range(0,n):

	b[a[i]]+=1;
#print(b)
		
for i in range(1,k+1):

	
	b[i]=b[i-1]+b[i]

		
#print(b)
for i in range(n-1,-1,-1):


	c[b[a[i]]-1]=a[i]

	b[a[i]]-=1
print("Sorted array is:")
print(c)



