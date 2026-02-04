#message=" hello   world "
#print(message.strip())
#print(message.upper())
#print(message.replace("world","python"))
#text="python programming"
#print(text[6::-1])
#print(text[:-6])
#print(text[0:6])
#print(text[0::3])
#sent="python programming"
#words=sent.split()
#print(words)
#new_se=""
#for word in words:
 #   new_se+=word[0].upper()+word[1:]+" "
#print(new_se.strip())

t=(5,10)
result=list(map(lambda x,y:x+y, t))
print(result)