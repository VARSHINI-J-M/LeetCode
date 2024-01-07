class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num=set(nums)
        leng=len(nums)
        result=[]
        for i in range(1,leng+1):
            if i not in num:
                result.append(i)
        return result
            