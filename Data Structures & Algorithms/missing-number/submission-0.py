class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        actual_sum=n*(n+1)//2
        for num in nums:
            actual_sum-=num
        
        return actual_sum