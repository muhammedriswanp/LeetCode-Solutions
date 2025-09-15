/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function (text, brokenLetters) {
    let words = text.split(" ")
    let count = 0;
    for (i = 0; i < words.length; i++) {
        let word = words[i];
        let canType = true;

        for (j = 0; j < brokenLetters.length; j++) {
            letters = brokenLetters[j];
            if (word.includes(letters)) {
                canType = false;
                break;
            }
        }
        if (canType) {
            count++
        }

    }
    return count;
};