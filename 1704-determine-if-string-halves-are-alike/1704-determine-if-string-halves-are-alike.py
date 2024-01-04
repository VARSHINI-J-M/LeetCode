class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        Vowels = 'aeiouAEIOU'
        
        aVowelsCount = 0
        for c in s[:len(s) // 2]:
            if c in Vowels:
                aVowelsCount += 1
        
        bVowelsCount = 0
        for c in s[len(s) // 2:]:
            if c in Vowels:
                bVowelsCount += 1
        
        return aVowelsCount == bVowelsCount
