
# f = open("a.txt","r")
# content = f.read()
# print(content)
# f.close()


with open("a.txt","r") as f:
    content = f.read()
    print(content)