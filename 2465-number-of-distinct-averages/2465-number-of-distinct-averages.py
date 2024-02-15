class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        sum=set()
        for i in range(n//2):
            a=nums[i]+nums[n-i-1]
            sum.add(a)
        return len(sum)