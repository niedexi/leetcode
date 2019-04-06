/*
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle 
is not part of haystack.

* @param {string} haystack
* @param {string} needle
* @return {number}
*/

var strStr = function(haystack, needle) {
    if (needle === "") {
        return 0;
    }
    for (let i = 0; i < (haystack.length - needle.length + 1); i++) {
        if (haystack.slice(i, (i + needle.length)) === needle) {
            return i;
        }
    }
    return -1;
};


var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
}
