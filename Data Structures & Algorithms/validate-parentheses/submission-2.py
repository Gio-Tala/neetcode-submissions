class Solution:
    def isValid(self, s: str) -> bool:
        corresponding_chars = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in corresponding_chars and len(stack) > 0 and corresponding_chars[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return not stack