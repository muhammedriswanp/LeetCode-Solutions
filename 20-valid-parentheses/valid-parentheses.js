/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
  const arr = [];

  const checkPara = {
    ")": "(",
    "}": "{",
    "]": "[",
  };

  for (let i = 0; i < s.length; i++) {
    const char = s[i];

    if (char === "(" || char === "{" || char === "[") {
      arr.push(char);
    } else {
      if (arr.length === 0) {
        return false;
      }

      const closing = arr.pop();

      if (checkPara[char] !== closing) {
        return false;
      }
    }
  }

  return arr.length === 0;
};

    
