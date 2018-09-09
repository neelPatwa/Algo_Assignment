def length_LCS(A,B):

	n=len(A)
	m=len(B)
	L=[[0]*(m+1) for k  in range(n+1) ]
	for i in range(0,n+1):
		
		for j in range(0,m+1):
			
			if i==0 or j==0:
				L[i][j]=0
			elif A[i-1]==B[j-1]:
				L[i][j]=1+L[i-1][j-1]
			else:
				L[i][j]=max(L[i-1][j],L[i][j-1])
		
	return L
def LCS(A,B,L,n,m):
	if n==0 or m==0:
		return ''
	elif A[n-1]==B[m-1]:
		return LCS(A,B,L,n-1,m-1)+A[n-1]
	elif L[n][m-1]>L[n-1][m]:
		return LCS(A,B,L,n,m-1)
	else:
		return LCS(A,B,L,n-1,m)
	
	
	


print("Enter String A")
A=raw_input()
print("Enter String B")
B=raw_input()

L=length_LCS(A,B)
print('Length Longest Common Subsequance is:'+str(L[len(A)][len(B)]))
print(LCS(A,B,L,len(A),len(B)))



	

