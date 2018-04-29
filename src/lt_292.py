"""
https://leetcode.com/problems/nim-game

Related:
  - lt_294_flip-game-ii
"""

"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
"""

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Time: O(1)
        # Space: O(1)
        return n % 4 != 0


if __name__ == '__main__':
    test_cases = [
        (1, True),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, True),
        (7, True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().canWinNim(test_case[0])
        print('output:', output)
        assert output == test_case[1]

