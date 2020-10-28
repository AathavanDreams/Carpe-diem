
day = int(input())
month = int(input())

weeks = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
line1 = []

k = 1
r=0 
m=day-1 
g=0
q=1

while k <= month:
    line1.append(k)
    k+=1

while r<m:
    line1.insert(r, '   ')
    r+=1
print (*weeks, sep=" ")
print (*line1, sep="   ")

while q<=6:
    while g<=7:
        p=line1[g]
        print(p)
        g+=1
        if g==7:
            print(p, sep="\n" )
    q+=1    

