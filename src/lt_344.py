# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    test_cases = [
        ('hello', 'olleh')
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseString(test_case[0])
        print('output:', output)
        assert output == test_case[1]

