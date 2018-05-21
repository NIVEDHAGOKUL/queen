a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
sum=0
for x in range(a,b):
  temp=x
  while(x>0):
    r=x%10
    n=n%10
    t=r*r*r
    sum=sum+t
    if(temp==sum):
    print (x)
   
  
