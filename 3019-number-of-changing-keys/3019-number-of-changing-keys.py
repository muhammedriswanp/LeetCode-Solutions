class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0 
        s = s.lower()
        for i, ch in enumerate(s) :
            if i == len(s) - 1:
                return count
            current = ch
            if current != s[i+1]:
                count += 1 
        return count
