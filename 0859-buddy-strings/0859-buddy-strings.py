class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        if s==goal and len(set(s))<len(s):
            return True
        
        lis=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                lis.append([s[i],goal[i]])

        if len(lis)==2 and lis[0]==lis[-1][::-1]:
            return True
        return False