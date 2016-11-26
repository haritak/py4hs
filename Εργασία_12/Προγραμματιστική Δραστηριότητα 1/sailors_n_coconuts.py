ok=False
n0=1
while not ok:
	n0+=5
	n1=4*(n0-1)/5
	if n1==int(n1):
		n2=4*(n1-1)/5
		if n2==int(n2):
			n3=4*(n2-1)/5
			if n3==int(n3):
				n4=4*(n3-1)/5
				if n4==int(n4):
					n5=4*(n4-1)/5
					if n5==int(n5):
						n6=(4*n5)/5
						ok=n6==int(n6)
print(n0,n0//5,n0%5)
print(int(n1),int(n1)//5,int(n1)%5)
print(int(n2),int(n2)//5,int(n2)%5)
print(int(n3),int(n3)//5,int(n3)%5)
print(int(n4),int(n4)//5,int(n4)%5)
print(int(n5),int(n5)//5,int(n5)%5)
