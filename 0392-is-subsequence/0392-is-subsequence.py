class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=len(s)
        if s1==0:
            return True
        s2=len(t)
        j=0
        count=0
        for i in range(s2):
            if j<s1 and s[j]==t[i]:
                count+=1
                j+=1
                if count==s1:
                    return True
        return False
                
                
            
        