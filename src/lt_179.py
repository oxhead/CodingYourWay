"""
https://leetcode.com/problems/largest-number

Related:
"""

"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Time: O(n*logn)
        # Space: O(1)
        return str(int(''.join(sorted(map(str, nums), key=lambda s: s*9)[::-1])))

    def largestNumber_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(n) for n in nums]
        # cmp(a, b) = (a > b) - (a < b)
        nums.sort(key=functools.cmp_to_key(lambda x, y: (y + x > x + y) - (y + x < x + y)))
        return ''.join(nums).lstrip('0') or '0'

    def largestNumber_failed(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def mycmp(n1, n2):
            s1 = str(n1)
            s2 = str(n2)
            if len(s1) > len(s2):
                if s1.startswith(s2) and s1.endswith('0'):
                    s2 = s2 + '9' * (len(s1) - len(s2))
            elif len(s1) < len(s2):
                if s2.startswith(s1) and s2.endswith('0'):
                    s1 = s1 + '9' * (len(s2) - len(s1))
            return (s1 > s2) - (s1 < s2)
        nums.sort(key=functools.cmp_to_key(mycmp), reverse=True) 
        output = ''.join([str(n) for n in nums])
        return output


if __name__ == '__main__':
    test_cases = [
        ([0, 0], "0"),
        ([3, 30, 34, 5, 9], "9534330"),
        ([121, 12], "12121"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().largestNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]

