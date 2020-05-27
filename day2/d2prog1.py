import math
x=int(input("Enter a number for all checkings:"))
flag=0;
if x%2==0:
    print("Number is Even")
else:
    print("Number is odd")
for i in range(2,int(x/2)):
    if x%i==0:
        flag=1
        break;
if flag==1:
    print("Number is not prime")
else:
    print("Number is prime")

rev=0
sumcube=0
i=x
while(i>0):
    a=i%10
    rev=rev*10+a
    sumcube=sumcube+math.pow(a,3)
    i=i//10
if sumcube==x:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
if rev==x:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
