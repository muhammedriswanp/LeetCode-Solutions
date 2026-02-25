class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        new_list = [ word for word  in words if word[::-1] == word ]
        if not new_list:
            return ""
        return new_list[0]