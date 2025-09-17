/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
    let newString = s.trim().split(" ")
    let lastWord = newString.length - 1
    let number= newString[lastWord].length

    return number
};