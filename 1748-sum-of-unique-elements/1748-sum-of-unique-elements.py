class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for index,value in enumerate(nums):
            if count[value]==1:
                ans+=value
        return ans
        