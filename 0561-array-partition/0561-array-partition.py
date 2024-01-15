class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        selected_elements = sorted_nums[::2]
        result = sum(selected_elements)
        return result
        