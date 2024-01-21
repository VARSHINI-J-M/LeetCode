class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n not in a:
            a.add(n)
            n=self.squares(n)
            if n==1:
                return True
        return False
    
    def squares(self,n):
        out=0
        while n:
            b=n%10
            b=b**2
            out+=b
            n=n//10
        return out

        