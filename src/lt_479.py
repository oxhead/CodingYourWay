"""
https://leetcode.com/problems/largest-palindrome-product

Related:
"""

"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""

class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # https://leetcode.com/problems/largest-palindrome-product/discuss/96305/Python-Solution-Using-Math-In-48ms
        if n==1: return 9
        if n==2: return 987
        for a in range(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0: continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337

    def largestPalindrome_bruteforce(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(1)
        # https://blog.csdn.net/shauna_wu/article/details/78247372 
        if n == 1: return 9
        upper = 10 ** n - 1
        for n1 in range(upper, upper//10, -1):
            p = str(n1)
            p = int(p + p[::-1])
            for n2 in range(upper, upper//10, -1):
                if p / n2 > upper: break
                if p % n2 == 0: return p % 1337 
        return -1


if __name__ == '__main__':
    test_cases = [
        (1, 9),
        (2, 9009 % 1337),
        (3, 906609 % 1337),
        (4, 99000099 % 1337),
        (5, 9966006699 % 1337),
        (6, 999000000999 % 1337),
        (7, 99956644665999 % 1337),
        (8, 9999000000009999 % 1337),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().largestPalindrome(test_case[0])
        print('output:', output)
        assert output == test_case[1]

