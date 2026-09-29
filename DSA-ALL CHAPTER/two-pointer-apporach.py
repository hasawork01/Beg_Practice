                         #Two pointer Apporach in sorted array to reverse an Array
                            # time complexity O(n)
                          # space Complexity O(1) 

# arr=[1,2,3,4,5]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left=left+1
#     right=right-1
# print(arr)


                            # sorted Array in two pointer apporach
                            # time complexity O(n)
                            # space complexity O(1)
                            
# arr=[1,2,3,4,5]
# target=7
# left=0
# right=len(arr)-1
# while left<right:
#     sum=arr[left]+arr[right]
#     if sum==target:
#         print(left,right)
#         break
#     elif sum<target:
#         left+=1
#     else:
#         right-=1


arr = [3, 2, 2, 3]
val = 3
i = 0
for j in range(len(arr)):
    if arr[j] != val:
        arr[i] = arr[j]
        i += 1
print(arr[:i])
print("Count =", i)
                            