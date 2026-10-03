class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
    
        before = [1] * n
        after = [1] * n
        answer = [1] * n

        for i in range(1, n):
            before[i] = before[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]

        for i in range(n):
            answer[i] = before[i] * after[i]
            
        return answer
