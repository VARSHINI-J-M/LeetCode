class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        i=nums.index(1)
        j=nums.index(n)
        if i > j:
            i-=1
        return i+(n-j-1)