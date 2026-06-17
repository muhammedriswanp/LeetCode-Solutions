class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        return sum(len(word) for word in words if Counter(word) <= char_count)
