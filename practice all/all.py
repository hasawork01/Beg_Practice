# name="hasan"

# print(name[::-1])


# name="hasan"
# for i in range(len(name)-1,-1,-1):
#     print(name[i])

# los=[1,2,3,4,5]
# i=0
# while(i<len(los)):
#     print(los[i])
#     i+=1

# for i in range(80):
#     print(i)

# lens=0
# while(lens<11):
#     print(lens)
#     lens+=1

                                        # function all print
                                        
# def num(n):
#     reverse=""
#     for i in range(len(n)-1,-1,-1):
#         reverse+=n[i]
        
#     return reverse
# print(num("hasan"))


def num(n):
    if(n==0):
        return 0
    return num(n-1)+n
n=int(input("enter the no"))

print(num(n))    

