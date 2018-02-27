"""
https://leetcode.com/problems/implement-strstr

Related:
  - lt_214
  - lt_459

Complexity:
  - Time: O()
  - Space: O()
"""

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        if not haystack: return -1

        index_haystack = 0
        index_needle = 0
        while index_haystack < len(haystack):
            index_found = index_haystack
            for c in needle:
                if index_found >= len(haystack):
                    return -1
                if c == haystack[index_found]:
                    index_found += 1
                else:
                    index_found = -1
                    break
            if index_found != -1:
                return index_haystack
            index_haystack += 1
        return -1

if __name__ == '__main__':
    test_cases = [
        (('', ''), 0),
        (('a', 'a'), 0),
        (('hello', 'll'), 2),
        (('aaaaa', 'bba'), -1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().strStr(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

