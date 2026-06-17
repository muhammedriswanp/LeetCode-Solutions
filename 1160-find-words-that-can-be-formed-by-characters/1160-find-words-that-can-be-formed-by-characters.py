class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        out = 0
        dit = {ch: chars.count(ch) for ch in set(chars)}

        for word in words:
            word_dit = {ch: word.count(ch) for ch in set(word)}

            valid = True

            for key, value in word_dit.items():
                if key not in dit or value > dit[key]:
                    valid = False
                    break

            if valid:
                out += len(word)

        return out