"""
https://leetcode.com/problems/shortest-word-distance-iii
https://leetcode.com/problems/shortest-word-distance

Related:
  - lt_243_shortest-word-distance
  - lt_244_shortest-word-distance-ii
"""

"""
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""

class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Time: O(n)
        # Space: (1)
        min_distance = float('inf')
        i1, i2 = -1, -1
        for i, word in enumerate(words):
            if word1 != word2:
                if word == word1:
                    i1 = i
                elif word == word2:
                    i2 = i
            else:
                if word != word1: continue
                if i1 == -1 and i2 == -1:
                    i1 = i
                elif i1 > i2:
                    i2 = i
                else:
                    i1 = i
            if i1 != -1 and i2 != -1:
                min_distance = min(min_distance, abs(i1 - i2))
        return min_distance
        

if __name__ == '__main__':
    test_cases = [
        ((["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"), 3),
        ((["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"), 1),
        ((["practice", "makes", "perfect", "coding", "makes"], "makes", "makes"), 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().shortestWordDistance(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

