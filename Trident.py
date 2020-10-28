t = int(input())  #height of prongs
s = int(input())  #spaces between prongs 
h = int(input())  #heigt of handle
r=s+1
for x in range (t):
    print("*" + s*" " + "*" + s*" " + "*")

print((3+(2*s))*"*")

for x in range (h):
    print((s+1)*" " + "*")