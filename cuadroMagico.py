def cuadro(M):
	D=[]
	sum=0
	for i in range(len(M)):
		s=0
		for j in range(len(M)):
			sum=sum+M[i][j]
			s=s+M[i][j]
		D.append(s)
	d=sum//2
	R=[]
	R.append(d-D[0])
	R.append(d-D[1])
	R.append(d-D[2])
	for i in range(len(M)):
		for j in range(len(M)):
			if i==j:
				M[i][j]=R[i]
				break
	return (M)
print(cuadro([[0,3,6],[5,0,5],[4,7,0]]))