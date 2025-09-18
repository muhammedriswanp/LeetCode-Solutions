/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    for (i = 0; i < nums.length; i++) {
        let number = nums[i]
        if (nums.indexOf(number) === nums.lastIndexOf(number)) {
            return number
        }
    }

    
};