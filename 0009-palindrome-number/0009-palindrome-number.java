class Solution {
    public boolean isPalindrome(int x) {
        int rem=0,n=x,rev=0;
        while(x>0)
        {
            rem=x%10;
            rev=(rev*10)+rem;
            x=x/10;
        }
        if(n==rev)
        {
            return true;
        }
        else{
            return false;
        }
    }
}