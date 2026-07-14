class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"(":")", "{": "}", "[": "]"}
        
        for c in s:
            if c in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if hashmap[opening] != c:
                    return False
        
        return not stack

