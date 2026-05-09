class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for OGindex, ind in enumerate(index):
            arr.insert(ind, nums[OGindex])
        return arr