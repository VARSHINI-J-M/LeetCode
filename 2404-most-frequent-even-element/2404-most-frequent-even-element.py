class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        a=0
        b=None
        cnt1=collections.Counter(nums)
        for i in sorted(cnt1.keys()):
            if i%2==0 and a<cnt1[i]:
                a=cnt1[i]
                b=i
        if b is None:
            return -1
        return b
        