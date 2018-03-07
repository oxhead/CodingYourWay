"""
https://leetcode.com/problems/ransom-note

Related:
  - lt_691_stickers-to-spell-word
"""

"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True

    def canConstruct_naive(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = {}
        for c in magazine:
            if c not in letters:
                letters[c] = 0
            letters[c] += 1
        for c in ransomNote:
            if c in letters and letters[c] > 0:
                letters[c] -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    test_cases = [
        (("a", "b"), False),
        (("aa", "ab"), False),
        (("aa", "aab"), True),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().canConstruct(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

