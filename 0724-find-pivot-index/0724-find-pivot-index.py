class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0

        for i,num in enumerate(nums):
            right = sum(nums[i+1:])
            if left == right :
                return i
            left += num
        return -1

            