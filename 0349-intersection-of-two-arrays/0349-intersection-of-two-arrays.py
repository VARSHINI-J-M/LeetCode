class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        num1=set(nums1)
        for num in nums2:
            if num in num1:
                result.append(num)
                num1.remove(num)
        return result
        