/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    string = ""
    for (i = 0; i < strs[0].length; i++) {
        let char = strs[0][i]
        for (j = 1; j < strs.length; j++) {
            if (strs[j][i] !== char) {
                return string
            }
        }
        string += char

    }
    return string
};