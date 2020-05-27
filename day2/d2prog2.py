def fib(n):
    if n<0:
        print("Put value greater than zero")
    elif n==0 or n==1:
        return(1)
    else:
        return(fib(n-1)+fib(n-2))

x=int(input("Enter the number up to which you wanna fibo:"))
for i in range(0,x+1):
    print(fib(i),end=",")

