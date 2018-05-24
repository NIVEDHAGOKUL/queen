int(input("Enter the number of elements:"))
m=[]
for i in range(1,n+1):
    a=int(input("Enter the number:"))
    m.append(a)
    print (m)
    for b in m:
       min=m[0]
    if(b<min):
      min=b
print(min)
