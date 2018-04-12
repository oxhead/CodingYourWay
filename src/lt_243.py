"""
https://leetcode.com/problems/shortest-word-distance

Related:
  - lt_244_shortest-word-distance-ii
  - lt_245_shortest-word-distance-iii
"""

"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        i1, i2 = -1, -1
        min_distance = float('inf')
        for i, word in enumerate(words):
            if word != word1 and word != word2:
                continue
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_distance = min(min_distance, abs(i1 - i2))
        return min_distance
        

if __name__ == '__main__':
    test_cases = [
        ((["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"), 3),
        ((["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"), 1),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().shortestDistance(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

