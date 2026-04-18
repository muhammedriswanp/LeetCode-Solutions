class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2
        
        a_count = sum(char in vowels for char in s[:mid])
        b_count = sum(char in vowels for char in s[mid:])
        
        return a_count == b_count
