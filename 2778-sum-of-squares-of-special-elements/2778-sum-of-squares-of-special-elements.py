class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum1=0
        n=len(nums)
        for i in range(n):
            if n % (i+1) ==0:
                sum1+=nums[i]**2
        return sum1
        