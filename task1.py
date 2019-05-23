f=open("Book1.txt","r")
f2=open("Book2.txt","w")
for line in f:
	f2.write(line)
