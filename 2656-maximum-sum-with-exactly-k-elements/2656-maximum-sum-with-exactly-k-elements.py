class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m=max(nums)
        tot=0
        for _ in range(k):
            tot+=m
            m+=1
        return tot