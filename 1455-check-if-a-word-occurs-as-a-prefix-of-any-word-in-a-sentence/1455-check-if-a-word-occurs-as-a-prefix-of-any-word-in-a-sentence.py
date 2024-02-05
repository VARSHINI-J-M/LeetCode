class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a = sentence.split()

        for i, j in enumerate(a):
            if j.startswith(searchWord):
                return i + 1

        return -1
        