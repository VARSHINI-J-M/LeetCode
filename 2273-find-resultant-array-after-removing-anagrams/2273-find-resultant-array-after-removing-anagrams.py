class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[words[0]]
        
        for i in range(1,len(words)):
            m1,m2=Counter(words[i-1]),Counter(words[i])
            if m1!=m2:
                result.append(words[i])
        return result