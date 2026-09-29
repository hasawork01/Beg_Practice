# n=int(input("enter the no:"))
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(f"factorial of no is: {fact(n)}")

n=int(input("enter the no"))
def num(n):
    if(n==0):
        return 1
    return num(n-1)*n
print(f"num is:{num(n)}")


# def number(a,b,c):
#     if(a>b and a>c):
#         print("a is greatest")
#     elif(b>a and b>c):
#         print("b is gratest")
#     else:
#         print("c is greatest")
# print(number)
# number(10,20,30)
                                        #Second Methods
                                        
                                        
# def number(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
# a=10
# b=20
# c=30
# print(f"greatest numberis:{number(a,b,c)}")

# def temp(t):
#     return 5*(t-32)/9
# t=int(input("enter the no"))
# print(temp(t))




