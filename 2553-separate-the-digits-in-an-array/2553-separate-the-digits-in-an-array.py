class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp=[]
        for num in nums:
            for i in str(num):
                temp.append(int(i))
        return temp