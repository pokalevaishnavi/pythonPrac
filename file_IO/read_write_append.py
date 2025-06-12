#read
f = open("a.txt","r")
content = f.read()

print(content)

f.close()


#write
f = open("b.txt","w")

string  =  '''
dr. Shaun Murphy is a good doctor who has autism.
He works in San Jose.
'''
f.write(string)
f.close()


#append

f = open("b.txt","a")

string  =  '''
Mr. Glassman is his best friend.
His coworksers are Browne,Park and Kalu.
'''
f.write(string)
f.close()





