
def longest_common_sub(A,B):
	if len(A)==1 or len(B)==1:
		if A[0]==B[0]:
			return 1
		else:
			return 0
	elif (A[0]==B[0]):
		return 1+longest_common_sub(A[1:],B[1:])
	elif (A[0])!=B[0]:
		return max(longest_common_sub(A[1:],B),longest_common_sub(A,B[1:]))

		

	




A=raw_input("Sequance 1:")
B=raw_input('Squuance 2:')
print('Max length of common subsequance is:'+str(longest_common_sub(A,B)))





	
