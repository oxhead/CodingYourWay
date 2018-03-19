"""
https://leetcode.com/problems/edit-distance

Related:
  - lt_161_one-edit-distance
  - lt_583_delete-operation-for-two-strings
  - lt_712_minimum-ascii-delete-sum-for-two-strings
"""

"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Time: O(m*n)
        # Space: O(m*n)
        # Wagner-Fischer algorithm
        # https://github.com/algorhythms/LeetCode/blob/master/072%20Edit%20Distance.py
        m, n = len(word1), len(word2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # insert, delete, replace
                    # insert: dp[i][j-1]
                    # abc  | abcb  | abc
                    #   b  |    b  |
                    # delete: dp[i-1][j]
                    # abc  | ab
                    #   b  |  b
                    # replace: dp[i-1][j-1]
                    # abc  | abb   | ab
                    #   b  |   b   |  
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[-1][-1]
        
        
    def minDistance_TLE(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def search(w1, w2):
            if len(w2) == 0: return len(w1)
            elif len(w1) < len(w2): return search(w2, w1)
            elif len(w2) == 1:
                count = len(w1) - 1 if w2 in w1 else len(w1)
                dp[(w1, w2)] = count
                return count

            count = float('inf')
            if w1[0] == w2[0]:
                count = search(w1[1:], w2[1:])
            else:
                count = min(1 + search(w1[1:], w2), 1 + search(w1[1:], w2[1:]))
            dp[(w1, w2)] = count
            return count
            
        dp = {}
        word1, word2= (word1, word2) if len(word1) >= len(word2) else (word2, word1)
        return search(word1, word2) 

if __name__ == '__main__':
    test_cases = [
        (("aaa", "abc"), 2),
        (("aaa", "abaa"), 1),
        (("aaa", "aa"), 1),
        (("baa", "aa"), 1),
        (("trinitrophenylmethylnitramine", "dinitrophenylhydrazine"), 10),
        
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minDistance(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
