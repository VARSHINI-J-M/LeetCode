class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        for i , c in enumerate(nums):
            if count[c]==1:
                return nums[i]
        