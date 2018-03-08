"""
https://leetcode.com/problems/compare-version-numbers

Related:
"""

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        size = max(version1.count('.'), version2.count('.'))
        version1 = version1 + ('.0' * (size - version1.count('.')))
        version2 = version2 + ('.0' * (size - version2.count('.')))
        n1 = tuple([int(n.lstrip('0')) if len(n) != n.count('0') else int(n) for n in version1.split('.')])
        n2 = tuple([int(n.lstrip('0')) if len(n) != n.count('0') else int(n) for n in version2.split('.')])
        return 0 if n1 == n2 else 1 if n1 > n2 else -1

if __name__ == '__main__':
    test_cases = [
        (('1.1', '0.1'), 1),
        (('0.1', '0.1'), 0),
        (('0.1', '1.1'), -1),
        (('1.0', '1'), 0),
        (('19.8.3.17.5.01.000', '19.8.3.17.5.01'), 0),
        (("19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000", "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000"), 0),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().compareVersion(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

