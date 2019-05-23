#Find the word that are not present in the book

f=open("20.txt","r")
print(f.read())
srch_word=input("enter any word:")
if(srch_word not in f):
	print("word not found.")
else:
	print("word found.")
