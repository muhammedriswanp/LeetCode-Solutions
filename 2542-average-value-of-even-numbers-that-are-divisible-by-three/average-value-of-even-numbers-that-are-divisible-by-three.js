/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    number=0
   count = 0
    for (i=0;i<nums.length;i++){

        if (nums[i]%6===0){
            
            number+=nums[i]
            count++
        }
    }
    if(count==0){
        return 0
    }
    return Math.floor(number/count)
};