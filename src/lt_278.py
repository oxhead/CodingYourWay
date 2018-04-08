"""
https://leetcode.com/problems/first-bad-version

Related:
  - lt_35_search-insert-position
"""

"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    return version >= VERSION

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    test_cases = [
        (10, 1),
        (10, 2),
        (10, 5),
        (10, 6),
        (10, 10),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        VERSION = test_case[1]
        output = Solution().firstBadVersion(test_case[0])
        print('output:', output)
        assert output == test_case[1]

