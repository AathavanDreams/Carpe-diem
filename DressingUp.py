rows = int(input())
columns = rows * 2

count = 1
odd = 1

while count < ((rows+1)/2):
        print ("*"*odd,end="")
        print (" "*(columns - (2*odd)), end="")
        print ("*"*odd)
        count+=1
        odd+=2          
else:
    odd == rows-2
    count == ((rows+1)/2) - 1

while count >= 1:
        print ("*"*odd,end="")
        print (" "*(columns - (2*odd)), end="")
        print ("*"*odd)        
        odd-=2
        count-=1

    