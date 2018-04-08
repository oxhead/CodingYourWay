"""
https://leetcode.com/problems/guess-number-higher-or-lower

Related:
  - lt_278_first-bad-version
  - lt_375_guess-number-higher-or-lower-ii
  - lt_658_find-k-closest-elements
"""

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example:

n = 10, I pick 6.

Return 6.
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    return 0 if ans == num else 1 if ans > num else -1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Time: O(logn)
        # Space: O(1)
        n_min, n_max = 1, n
        while True:
            mid = (n_min + n_max) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                n_min = mid + 1
            else:
                n_max = mid - 1


if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (2, 1),
        (2, 2),
        (3, 3),
        (10, 6),
        (1000, 50),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        ans = test_case[1]
        output = Solution().guessNumber(test_case[0])
        print('output:', output)
        assert output == test_case[1]

