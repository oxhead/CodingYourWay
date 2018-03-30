"""
https://leetcode.com/problems/group-anagrams

Related:
  - lt_242_valid-anagram
  - lt_249_group-shifted-strings
"""

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.
"""

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time: O(n * klogk)
        # Space: O(n)
        output = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in output:
                output[key] = []
            output[key].append(s)
        return [group for group in output.values()]


if __name__ == '__main__':
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat","tea"], ["nat","tan"], ["bat"]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().groupAnagrams(test_case[0])
        print('output:', output)
        assert sorted([sorted(group) for group in output]) == sorted([sorted(group) for group in test_case[1]])

