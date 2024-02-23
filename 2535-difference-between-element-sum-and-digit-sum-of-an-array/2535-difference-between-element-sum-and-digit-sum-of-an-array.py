class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_e=sum(nums)
        digit_s=0
        temp=''
        for num in nums:
            temp+=str(num)
        temp=list(temp)
        for i in temp:
            digit_s+=int(i)
        return abs(sum_e-digit_s)
        
            
        