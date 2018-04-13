"""
https://leetcode.com/problems/word-ladder-ii

Related:
  - lt_127_word-ladder
"""

"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
"""

import collections

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # Time: O(?)
        # Space: O(?)
        # https://leetcode.com/problems/word-ladder-ii/discuss/40458/Use-defaultdict-for-traceback-and-easy-writing-20-lines-python-code
        wordSet = set(wordList)
        traces = collections.defaultdict(set)
        level = set([beginWord])
        while level and endWord not in traces:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in range(len(beginWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                         candidate = word[:i] + c + word[i+1:]
                         if candidate != word:
                             if candidate in wordSet and candidate not in traces:
                                 next_level[candidate].add(word)
            level = next_level
            traces.update(next_level)
        output = [[endWord]]
        while output and output[0][0] != beginWord:
            output = [[previous_word] + path for path in output for previous_word in traces[path[0]]]
        return output
        
    def findLadders_failed(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordDict = set(wordList)
        if endWord not in wordDict: return []
        output = [[beginWord]]
        candidates = [beginWord]
        visited = set([beginWord])
        while candidates:
            found = [word for word in candidates if endWord == word]
            if found:
                print('@ matched')
                return [sub for word in found for sub in output if sub[-1] == word]
                            
            queue = {}
            matched = False
            visited_new = set()
            for word in candidates:
                queue[word] = []
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + c + word[i+1:]
                        if candidate in wordDict and candidate not in visited:
                            queue[word].append(candidate)
                            visited.add(candidate)
                            matched = True
                if matched:
                    visited.remove(word)
                    visited_new.add(word)
            visited = visited | visited_new

            print('# queue:', queue)
            output_new = []
            for previous, words in queue.items():
                for w in words:
                    for sub in output:
                        if sub[-1] == previous:
                            output_new.append(sub + [w])
            output = output_new
            for sub in output:
                print(sub)
            candidates = []
            for l in queue.values():
                for w in l:
                    candidates.append(w)
            print('candidates:', candidates)
            print('visited:', visited)
        return []

if __name__ == '__main__':
    test_cases = [
        (("hit", "cog", ["hot","dot","dog","lot","log","cog"]), [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findLadders(*test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])

