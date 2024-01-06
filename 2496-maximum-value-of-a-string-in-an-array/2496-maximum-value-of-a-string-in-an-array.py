class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0
        for s in strs:
            if any(c.isalpha() for c in s):
                max_value = max(max_value, len(s))
            else:
                max_value = max(max_value, int(s))
        return max_value
