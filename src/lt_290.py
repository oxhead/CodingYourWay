"""
https://leetcode.com/problems/word-pattern
https://leetcode.com/problems/isomorphic-strings

Related:
  - lt_205_isomorphic-strings
  - lt_291_word-pattern-ii
"""

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 
"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        if len(pattern) != len(str.split()): return False
        mapping = {}
        used = set()
        for c, word in zip(list(pattern), str.split()):
            if c in mapping and mapping[c] != word:
                return False
            if c not in mapping and word in used:
                return False
            mapping[c] = word
            used.add(word)
        return True


if __name__ == '__main__':
    test_cases = [
        (("abba", "dog cat cat dog"), True),
        (("abba", "dog cat cat fish"), False),
        (("aaaa", "dog cat cat dog"), False),
        (("abba", "dog dog dog dog"), False),
        (("aaa", "aa aa aa aa"), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().wordPattern(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

