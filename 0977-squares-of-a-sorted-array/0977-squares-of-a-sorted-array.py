class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[]
        for i in range(len(nums)):
            sq1=nums[i]*nums[i]
            sq.append(sq1)
        sq.sort()
        return sq
            
            
        