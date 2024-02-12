class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans=''
        l=len(s)
        for i in range(l//2):
            ans+=s[i]
            if l % len(ans)==0:
                if ans*(l//len(ans))==s:
                    return True
        return False