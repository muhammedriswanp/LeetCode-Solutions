class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = {}
        good_pairs = 0
        
        for num in nums:
            if num in counts:
                good_pairs += counts[num]
                counts[num] += 1
            else:
                counts[num] = 1
                
        return good_pairs
