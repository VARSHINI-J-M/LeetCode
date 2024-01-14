class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    a = len(nums)

    for i, num in enumerate(nums):
      a ^= i ^ num

    return a