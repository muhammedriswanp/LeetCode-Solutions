class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = { }
        for index, num in enumerate(nums):
            req_num = target - num
            if req_num in dic:
                return [dic[req_num],index]

            dic[num] = index