class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count1=collections.Counter(target)
        count2=collections.Counter(arr)
        if count1!=count2:
            return False
        else:
            return True
        