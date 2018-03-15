"""
https://leetcode.com/problems/judge-route-circle

Related:
  - lt_547_friend-circles
"""

"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:

Input: "UD"
Output: true

Example 2:

Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

    def judgeCircle_verbose(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(1)
        if not moves: return False
        p = [0, 0]
        for action in moves:
            if action == 'R': p[1] += 1
            elif action == 'L': p[1] -= 1
            elif action == 'U': p[0] -= 1
            elif action == 'D': p[0] += 1
        return p == [0, 0]

if __name__ == '__main__':
    test_cases = [
        ("UD", True),
        ("LL", False),
        ("DURDLDRRLL", False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().judgeCircle(test_case[0])
        print('output:', output)
        assert output == test_case[1]

