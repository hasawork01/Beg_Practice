                                                        # Two Sum
class Solution:
    def twoSum(self,arr,target):
        for i in arr(i,arr-1):
            for j in range(i+1,arr):
                if(arr[i]+arr[j]==target):
                    return[i,j]
                