class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num=set(nums)
        b=-1
        for n in nums:
            if n>0 and -n in num:
                b=max(b,n)
        return b  
        
        
        