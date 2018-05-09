"""
https://leetcode.com/problems/palindrome-pairs

Related:
  - lt_5_longest-palindromic-substring
  - lt_214_shortest-palindrome
"""

"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Time: O(n * k^2)
        # Space: O(n * k)
        # https://www.jianshu.com/p/fcde442da61b
        def is_palindrome(word):
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]: return False
                left += 1
                right -= 1
            return True
        output = []
        records = {}
        for i, word in enumerate(words):
            records[word[::-1]] = i
        for i, word in enumerate(words):
            for j in range(len(word)):
                w1 = word[:j] 
                w2 = word[j:]
                if w1 in records and records[w1] != i and is_palindrome(w2):
                    output.append([i, records[w1]]) 
                    if w1 == '':
                        output.append([records[w1], i])
                if w2 in records and records[w2] != i and is_palindrome(w1):
                    output.append([records[w2], i])
        return output
           

if __name__ == '__main__':
    test_cases = [
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
        (["a","abc","aba",""], [[0,3],[3,0],[2,3],[3,2]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().palindromePairs(test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])

