class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        letters=set(jewels)
        count=0

        for char in stones:
            if char in letters:
                count+=1
        
        return count
