n=int(input("Enter the number of elements:"))
m=[]
for i in range (1,n+1):
    a=int(input("Enter the number:"))
    m.append(a)
    m.sort()
    print(m)
