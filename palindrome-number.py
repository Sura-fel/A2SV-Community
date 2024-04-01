class Solution:
    def isPalindrome(self, x: int) -> bool:
        y, z = 0, x
        while x > 0:
            y = y*10 + x%10
            x = x//10
        return z == y
