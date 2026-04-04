class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = [ ]
        wight = 0 

        for num in nums:
            for n in nums:
                if num > n :
                    wight+=1
            c.append(wight)
            wight = 0
        return c
