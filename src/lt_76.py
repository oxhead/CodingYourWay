"""
https://leetcode.com/problems/minimum-window-substring

Related:
  - lt_30_substring-with-concatenation-of-all-words
  - lt_209_minimum-size-subarray-sum
  - lt_239_sliding-window-maximum
  - lt_567_permutation-in-string
  - lt_632_smallest-range
  - lt_727_minimum-window-subsequence
"""

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Time: O(n)
        # Space: O(k)
        records = {}
        for c in t:
            if c not in records: records[c] = 0
            records[c] += 1
        left, right = 0, 0
        cursor = 0
        count = len(t)
        min_count = float('inf')
        min_left = 0
        for i, c in enumerate(s):
            if c in records:
                if records[c] > 0: count -= 1
                records[c] -= 1
            while count <= 0:
                if right - left + 1 < min_count:
                    min_count = right - left + 1
                    min_left = left
                if s[left] in records:
                    records[s[left]] += 1
                    if records[s[left]] > 0: count += 1
                left += 1
            right += 1
        return s[min_left:min_left+min_count] if min_count != float('inf') else ''

    def minWindow_failed(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        character_set = set(t)
        indexs = {}
        min_window = float('inf')
        output = ""
        for i, c in enumerate(s):
            if c not in character_set: continue
            indexs[c] = i
            if len(indexs) == len(character_set):
                index_left = min(indexs.values())
                index_right = max(indexs.values())
                if index_right - index_left < min_window and index_right - index_left + 1 >= len(t):
                    output = s[index_left:index_right+1]
                    min_window = len(output)
        return output 

if __name__ == '__main__':
    test_cases = [
        (("ADOBECODEBANC", "ABC"), "BANC"),
        (("a", "aa"), ""),
        (("aa", "aa"), "aa"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minWindow(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

