"""
https://leetcode.com/problems/shortest-word-distance-ii
https://leetcode.com/problems/shortest-word-distance

Related:
  - lt_21_merge-two-sorted-lists
  - lt_243_shortest-word-distance
  - lt_245_shortest-word-distance-iii
"""

"""
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
import collections

class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # Time: O(n)
        self.records = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.records[word].append(i)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Time: O(a + b), a and b are the number of word1's and word2's occurence
        index_list1 = self.records[word1]
        index_list2 = self.records[word2]
        i, j, min_distance = 0, 0, float('inf')
        while i < len(index_list1) and j < len(index_list2):
            min_distance = min(min_distance, abs(index_list1[i] - index_list2[j]))
            if index_list1[i] < index_list2[j]:
                i += 1
            else:
                j += 1
        return min_distance


class WordDistance_TLE:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.records = {}
        self._build()
    
    def _build(self):
        word_list = list(set(self.words))
        for word1 in word_list:
            for word2 in word_list:
                if word1 != word2:
                    self._shortest(word1, word2) 
        
    def _shortest(self, word1, word2):
        i1, i2 = -1, -1
        min_distance = float('inf')
        for i, word in enumerate(self.words):
            if word not in (word1, word2):
                continue
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_distance = min(min_distance, abs(i1 - i2))
        self.records[(word1, word2)] = min_distance
        self.records[(word2, word2)] = min_distance

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.records: return self.records[(word1, word2)]
        else: return -1


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

if __name__ == '__main__':
    test_cases = [
        ((["practice", "makes", "perfect", "coding", "makes"], [("coding", "practice"), ("makes", "coding")]), [3, 1]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        words = test_case[0][0]
        obj = WordDistance(words)
        for word_pair, answer in zip(test_case[0][1], test_case[1]):
            output = obj.shortest(*word_pair)
            print('word1={}, word2={}, output={}'.format(word_pair[0], word_pair[1], output))
            assert output == answer

