class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            w1=word[::-1]
            if word == w1:
                return word
        return ""