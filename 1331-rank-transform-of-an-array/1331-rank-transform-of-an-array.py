class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    a = {}

    for b in sorted(arr):
      if b not in a:
        a[b] = len(a) + 1

    return map(a.get, arr)