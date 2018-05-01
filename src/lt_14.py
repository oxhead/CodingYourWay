"""
https://leetcode.com/problems/longest-common-prefix

Related:
"""

"""
Write a function to find the longest common prefix string amongst an array of strings. 
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Time: O(n * k)
        # Space: O(1)
        if not strs: return ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if (i < len(s) and s[i] != c) or i >= len(s):
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix_v2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        str_template = strs[0]
        index = -1
        for i, s in enumerate(str_template):
            if not all(map(lambda str_other: str_other[i] == s if i < len(str_other) else False, strs[1:])):
                break
            index = i
        return str_template[:index+1] if index >= 0 else ''


if __name__ == '__main__':
    test_cases = [
        (['a', 'b'], ''),
        (['aa', 'ab'], 'a'),
        (['aaa', 'aab'], 'aa'),
        (['abaa', 'abab'], 'aba'),
        (['aa', 'a'], 'a'),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestCommonPrefix(test_case[0])
        print('output:', output)
        assert output == test_case[1]

