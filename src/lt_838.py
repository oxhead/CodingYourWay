"""
https://leetcode.com/problems/push-dominoes
"""

"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Note:

    0 <= N <= 10^5
    String dominoes contains only 'L', 'R' and '.'
"""

class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # Time: O(n)
        # Space: O(n)
        nums = [0 if c == '.' else 1 if c == 'R' else -1 for c in dominoes]
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1: current = 1
            elif nums[i] == -1: current = 0
            if nums[i] == 0 and current >= 1:
                current += 1
                nums[i] += current
        current = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == -1: current = -1
            elif nums[i] == 1: current = 1
            elif current <= -1:
                current -= 1
                if nums[i] == 0: nums[i] = current
                elif abs(current) < abs(nums[i]):
                    nums[i] = current
                elif abs(current) == abs(nums[i]):
                    nums[i] = 0
                else: continue
        return "".join(["." if n == 0 else "R" if n > 0 else "L" for n in nums])
                

if __name__ == '__main__':
    test_cases = [
        (".L.R...LR..L..", "LL.RR.LLRRLL.."),
        ("RR.L", "RR.L"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().pushDominoes(test_case[0])
        print('output:', output)
        assert output == test_case[1]
