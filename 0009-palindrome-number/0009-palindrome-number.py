class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        forward = []
        for i in range(0, len(str(x))):
            forward.append(str(x)[i])
        
        reverse = []
        j = len(str(x)) - 1
        for _ in range(len(str(x)), 0, -1):
            reverse.append(str(x)[j])
            j -= 1
            
        if forward == reverse:
            return True
        else:
            return False
            