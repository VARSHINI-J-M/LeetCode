class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t=list(set(nums))
        r=sorted(t, reverse=True)
        if (len(r) < 3):
            return r[0]
        else:
            return r[2]