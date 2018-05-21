n=int(input("Enter the number:"))
temp=n
sum=0
while(n>0):
    r=n%10
    t=r**3
    sum=sum+t
    n=n//10
    if(sum==temp):
        print("armstrong")
else:
    print("Not armstrong")

