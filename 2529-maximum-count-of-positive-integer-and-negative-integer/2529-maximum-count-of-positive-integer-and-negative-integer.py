class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cnt_p=0
        cnt_n=0
        for i in nums:
            if i>0:
                cnt_p+=1
            elif i<0:
                cnt_n+=1
        return max(cnt_p,cnt_n)
        