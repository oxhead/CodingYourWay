"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

Related:
"""

"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

class TrieNode:
    def __init__(self):
        self.bits = [None, None]

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        # http://hankerzheng.com/blog/LeetCode-Maximum-XOR-of-Two-Numbers-in-an-Array
        mask = 0
        ans = 0
        for bit in range(31, -1, -1):
            mask |= 1 << bit
            prefix_set = {num & mask for num in nums}
            guess = ans | 1 << bit
            for prefix in prefix_set:
                if prefix ^ guess in prefix_set:
                    ans = guess
        return ans

    def findMaximumXOR_bruteforce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                max_val = max(max_val, nums[i] ^ nums[j])
        return max_val

    def findMaximumXOR_trie(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        trie = TrieNode()
        for n in nums:
            current = trie
            for i in range(31, -1, -1):
                bit = (n >> i) & 1
                if current.bits[bit] == None:
                    current.bits[bit] = TrieNode()
                current = current.bits[bit]
        max_value = 0
        for n in nums:
            current = trie
            value = 0
            for i in range(31, -1, -1):
                bit = (n >> i) & 1
                if current.bits[bit ^ 1] != None:
                    value += (1 << i)
                    current = current.bits[bit ^ 1]
                else:
                    current = current.bits[bit]
            max_value = max(max_value, value)
        return max_value 


if __name__ == '__main__':
    test_cases = [
        ([3, 10, 5, 25, 2, 8], 28),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findMaximumXOR(test_case[0])
        print('output:', output)
        assert output == test_case[1]

