class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f"{n:032b}"
        r = binary[::-1]

        return int(r,2)
