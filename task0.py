#To https://github.com/Abhi1296/FizzBuzz.git
# * [new branch]      master -> master
#pBranch master set up to track remote branch master from task0.py

def func1(num1):
	#while num1!=100
	#	print(num1)
	#	num1+=1
	#return num1
	
	if num1%3==0:
	    return "Fizz"
	elif num1%5==0:
	    return "Buzz"
	elif num1%3==0 and num1%5==0:
	    return "FizzBuzz"
for n in range(1,101):
	print(func1(num1))
