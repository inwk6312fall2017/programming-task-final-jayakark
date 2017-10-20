op=open("running-config.cfg","r")
line=op.read()

word=line.replace("172","192")
op1=open("replace.txt","w")
op1.write(word)
print("written, please check replace.txt")