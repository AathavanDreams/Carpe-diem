
start = int(input())
days = int(input())

print("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", sep="\t")

nadkal = 1
space = start - 1

for x in range (space):
    print ("\t", end="")

while nadkal <= days:
    if start == 7:
        print (nadkal, end="\n")
        start = 1
    else:
        print (nadkal, end="\t") 
        start+=1    
    nadkal+=1 