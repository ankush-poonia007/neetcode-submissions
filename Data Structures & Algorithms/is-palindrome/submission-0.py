class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char.lower())
            
        return stack[::-1] == stack[::]
            
            