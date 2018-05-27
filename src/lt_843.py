"""
https://leetcode.com/contest/weekly-contest-86/problems/guess-the-word/
"""

"""
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.

Note:  Any solutions that attempt to circumvent the judge will result in disqualification.
"""

import collections
import itertools

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def __init__(self, secret, word_list):
        self.secret = secret
        self.word_list = set(word_list)
        self.hit = False
        self.count = 0

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        def match(a, b):
            matches = 0;
            for i in range(len(a)):
                if a[i] == b[i]: matches += 1
            return matches
        self.count += 1
        if word not in self.word_list: return -1
        if word == self.secret: self.hit = True
        return match(word, self.secret)


class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(a, b):
            matches = 0;
            for i in range(len(a)):
                if a[i] == b[i]: matches += 1
            return matches
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if match(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if match(w, guess) == n] 
        

if __name__ == '__main__':
    test_cases = [
        (("acckzz", ["acckzz","ccbazz","eiowzz","abcczz"]), None)
    ]

    for test_case in test_cases:
        print('case:', test_case)
        master = Master(*test_case[0])
        output = Solution().findSecretWord(test_case[0][1], master)
        print('output:', master.hit and master.count <= 10)
        assert output == test_case[1]
