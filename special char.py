
n=input('Enter the string:')
digit=0
letter=0
others=0
t=len(n)
for i in range(0,t):
    if(n[i].isdigit()):
        digit+=1
    elif(n[i].isalpha()):
        letter+=1
    else:
        others+=1
print(others)



