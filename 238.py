# Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
#         l_arr = [0] * n
#         r_arr = [0] * n
#         l_arr[0] = 1
#         r_arr[-1] = 1
        
#         for i in range(1,n):
#             l_arr[i] = l_arr[i-1] * nums[i-1]
            
#         for i in range(n-2, -1, -1):
#             r_arr[i] = r_arr[i+1] * nums[i+1]
            
#         for i in range(n):
#             l_arr[i] *= r_arr[i]
            
#         return l_arr
        
        arr = [0] * len(nums)
        arr[0] = 1
        
        for i in range(1,n):
            arr[i] = arr[i-1] * nums[i-1]
            
        r = 1
        for i in range(n-1, -1, -1):
            arr[i] = arr[i] * r
            r *= nums[i]
            
        return arr
