class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        t=str(x)
        if x<0:
            return False
        else:
            if t == y[::-1]:
                return True
            else:
                return False    
