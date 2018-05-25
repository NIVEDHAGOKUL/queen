n=int(input("Enter the number:"))
a=0
b=1
for i in (0,n):
    print(a)
    c=a+b
    a=b
    b=c
print(c)
