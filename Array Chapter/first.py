# arr=[10,20,30]
# print(arr)
# # arr.update(2,30)
# arr[2]=100
# print(arr)
# arr.remove(10)
# print(arr)
# print(len(arr))
# for i in arr:
#     print(arr[i])
# for i in range(len(arr)):
#     print(arr[i])

                                        # MAXIMUM ELEMENT NUMBER OF THE ARRAY
# arr=[10,20,30,40]
# maximum=arr[0]
# for i in arr:
#     if(i>maximum):
#         maximum=i
# print(maximum)


                                      #   MINIMUM ELEMENT NUMBER OF THE ARRAY 
                                      
# arr=[10,20,50,30,5]
# minimum=arr[0]
# for i in arr:
#     if i<minimum:
#         minimum=i
# print(minimum)

                                            #TOTAL ELEMENT OF SUM ARRAY
                                            
                                        
# arr=[20,30,50,60,10]
# total=0
# for i in arr:
#     total+=i
# print(total)

                            # array input and print

# arr=list(map(int,input("enter the no").split()))
# ind=0
# # arr=[10,20,30,40]
# for value in arr:
#     print(ind,value)
#     ind=ind+1                

arr=[10,20,30,40,50]
reverse=[]
for i in range(len(arr)-1,-1,-1):
    reverse.append(arr[i])
print(reverse)                    
                            
                            