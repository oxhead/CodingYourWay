"""
https://leetcode.com/contest/weekly-contest-84/problems/find-and-replace-in-string/
"""

"""
To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".

Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.

All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.

Example 1:

Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
"ed" starts at index 2 in S, so it's replaced by "ffff".

Example 2:

Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee". 
"ec" doesn't starts at index 2 in the original S, so we do nothing.

Notes:

    0 <= indexes.length = sources.length = targets.length <= 100
    0 < indexes[i] < S.length <= 1000
    All characters in given inputs are lowercase letters.
"""

class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        ops = list(zip(indexes, sources, targets))
        ops.sort(key=lambda x: x[0])
        valid_ops = []
        for index, source, target in ops:
            pos = S.find(source, index)
            if pos == -1 or pos != index: continue
            valid_ops.append((index, source, target))
        s = ""
        previous_index = 0
        for index, source, target in valid_ops:
            if index > previous_index:
                s += S[previous_index:index]
            s += target
            previous_index = index+len(source)
        if previous_index < len(S):
            s += S[previous_index:]
        return s

        
if __name__ == '__main__':
    test_cases = [
        (("abcd", [0,2], ["a","cd"], ["eee","ffff"]), "eeebffff"),
        (("abcd", [0,2], ["ab","ec"], ["eee","ffff"]), "eeecd"),
        (("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]), "vbfrssozp"),
        (("wreorttvosuidhrxvmvo", [14,12,10,5,0,18], ["rxv","dh","ui","ttv","wreor","vo"], ["frs","c","ql","qpir","gwbeve","n"]), "gwbeveqpirosqlcfrsmn"),
        (("jjievdtjfb", [4,6,1], ["md","tjgb","jf"], ["foe","oov","e"]), "jjievdtjfb"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().findReplaceString(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
