class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for c in s:
            if c in CloseToOpen :
                if  not stack or stack.pop() != CloseToOpen[c]:
                    return False 
            else :
                stack.append(c)
        return not stack