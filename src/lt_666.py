"""
https://leetcode.com/problems/path-sum-iv

Related:
  - lt_112_path-sum
  - lt_113_path-sum-ii
  - lt_124_binary-tree-maximum-path-sum
  - lt_437_path-sum-iii
"""

"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

    The hundreds digit represents the depth D of this node, 1 <= D <= 4.
    The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
    The units digit represents the value V of this node, 0 <= V <= 9.

Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
"""

from utils import parse_tree

class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n), equal to O(2^logn)=O(n)
        # Space: O(n)
        def search(node, count):
            if node not in records: return 0
            elif (node[0] + 1, (node[1] - 1) * 2 + 1) not in records and (node[0] + 1, (node[1] - 1) * 2 + 2) not in records:
                return count + records[node]
            else:
                return search((node[0] + 1, (node[1] - 1) * 2 + 1), count + records[node]) + search((node[0] + 1, (node[1] - 1) * 2 + 2), count + records[node])
        records = {}
        for num in nums:
            D, P, V = num//100, num//10%10, num%10
            records[(D, P)] = V
        return search((1, 1), 0)

    def pathSum_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def path_sum(d, p, total):
            if (d, p) not in records:
                return None
            elif (d + 1, (p - 1) * 2 + 1) not in records and (d + 1, (p - 1) * 2 + 2) not in records:
                return total + records[(d, p)]
            total += records[(d, p)]
            s1 = path_sum(d + 1, (p - 1) * 2 + 1, total)
            s2 = path_sum(d + 1, (p - 1) * 2 + 2, total)
            count = 0
            if s1 != None: count += s1
            if s2 != None: count += s2
            return count

        if not nums: return 0
        records = {}
        for n in nums:
            records[(n // 100, n % 100 // 10)] = n % 10
        return path_sum(1, 1, 0)


if __name__ == '__main__':
    test_cases = [
        ([113, 215, 221], 12),
        ([113, 221], 4),
        ([119, 213, 321, 430], 13),
        ([113, 229, 349, 470, 485], 47)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().pathSum(test_case[0])
        print('output:', output)
        assert output == test_case[1]

