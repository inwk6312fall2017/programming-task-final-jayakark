import re
op1=open("Book1.txt","r")
book1=op1.read()

longest1=0
for i in book1.split("."):
    b=i.split()
    for re in range(len(b)):
     if len(b[re]) > longest1:
            longest1 = len(b[re])
            longest_word1 = b[re]
print("Longest word from book1 is :  ",longest_word1)

op2=open("Book2.txt","r")
book2=op2.read()
A=[]
longest2=0
for i in book2.split('.'):
    b=i.split()
    for re in range(len(b)):
     if len(b[re]) > longest2:
            longest2 = len(b[re])
            longest_word2 = b[re]
print("Longest word from book2 is :  ",longest_word2)

op3=open("Book3.txt","r")
book3=op3.read()

longest3=0
for i in book3.split('.'):
    b=i.split()
    for re in range(len(b)):
     if len(b[re]) > longest3:
            longest3 = len(b[re])
            longest_word3 = b[re]
print("Longest word from book1 is :  ",longest_word3)

if (longest_word1>longest_word2>longest_word1):
    print("biggest word is",longest_word1)
elif (longest_word2>longest_word3):
    print("Biggest word is",longest_word2)
else:
         print("Biggest word is ",longest_word3)

#ma=max(longest_word1,longest_word2,longest_word3)
#print(ma)