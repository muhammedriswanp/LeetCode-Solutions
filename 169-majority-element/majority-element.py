class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        current_num = None
        for num in nums:
            if count == 0:
                current_num = num

            if num == current_num  :
                count+=1
            else :
                count-=1

        return current_num