"""
https://leetcode.com/problems/sentence-similarity-ii

Related:
  - lt_547_friend-circles
  - lt_721_accounts-merge
  - lt_734_sentence-similarity
"""

"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:
The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # Time: O(n + p), ?
        # Space: O(n + p)
        class DisjointSet:
            def __init__(self, n):
                self.set = [i for i in range(n)]

            def find_set(self, x):
                if self.set[x] != x:
                    self.set[x] = self.find_set(self.set[x])
                return self.set[x]

            def union_find(self, x, y):
                x_root, y_root = map(self.find_set, (x, y))
                if x_root != y_root:
                    self.set[min(x_root, y_root)] = max(x_root, y_root)

            def is_disjoint(self, x, y):
                return self.find_set(x) != self.find_set(y)

        if len(words1) != len(words2): return False
        words = set()
        for p1, p2 in pairs:
            words.add(p1)
            words.add(p2)
        for w1 in words1:
            words.add(w1)
        for w2 in words2:
            words.add(w2)
        words = {w: i for i, w in enumerate(words)}
        ds = DisjointSet(len(words))
        for p1, p2 in pairs:
            ds.union_find(words[p1], words[p2])
        for w1, w2 in zip(words1, words2):
            if ds.is_disjoint(words[w1], words[w2]):
                return False
        return True

    def areSentencesSimilarTwo_dfs(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # Time: O(n + p)
        # Space: O(p)
        if len(words1) != len(words2): return False
        def traverse(target, root):
            if target in records: return
            records[target] = root
            for next_target in words[target]:
                traverse(next_target, root)
        from collections import defaultdict
        words = defaultdict(set)
        for p1, p2 in pairs:
            words[p1].add(p2)
            words[p2].add(p1)

        records = {}
        for word in words.keys():
            traverse(word, word)

        for w1, w2 in zip(words1, words2):
            if records.get(w1, w1) != records.get(w2, w2):
                return False
        return True


if __name__ == '__main__':
    test_cases = [
        ((["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]), True),
        ((["an","extraordinary","meal","meal"], ["one","good","dinner"], [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]), False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().areSentencesSimilarTwo(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

