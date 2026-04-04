class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = [ ]
        

        for num in nums:
            wight = 0 
            for n in nums:
                if num > n :
                    wight+=1
            c.append(wight)
           
        return c
