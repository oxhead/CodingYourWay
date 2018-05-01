"""
https://leetcode.com/problems/longest-palindromic-substring

Related:
  - lt_214_shortest-palindrome
  - lt_266_palindrome-permutation
  - lt_336_palindrome-pairs
  - lt_516_longest-palindromic-subsequence
  - lt_647_palindromic-substrings
"""

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

 

Example:

Input: "cbbd"

Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time: O(n^2)
        # Space: O(n^2)
        # Hint: (1) The naive way is to do bruteforce for each substring and then
        #       check whether its a palindrome or not
        #       (2) Find the repitive structure and then use DP to reuse results
        # Example: abcba
        # size = 1
        # a b c b a
        # 1 1 1 1 1
        # size = 2
        # a b c b a
        # 0 0 0 0 0
        # size = 3
        # a b c b a (should use 2-d array to record substring)
        # 0 0 0 3 b
        # size = 4
        # a b c b a
        # 0 0 0 0 0
        # size = 5
        # a b c b a
        # 0 0 0 0 5 (because s[0] == s[4] and s[3] == 1)
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        for size in range(1, n+1):
            i = 0
            j = i + size - 1
            while j < n: 
                if i == j:
                    dp[i][j] = 1
                elif j - i == 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 1 if s[i] == s[j] and dp[i+1][j-1] else 0
                i += 1
                j += 1

        for size in range(n, 0, -1):
            i, j = 0, size - 1
            while j < n:
                if dp[i][j] == 1: return s[i:j+1]
                i += 1
                j += 1
        return ''

    def longestPalindrome_dp_earlystop(self, s):
        """
        :type s: str
        :rtype: str
        """
        def search(i, j):
            if dp[i][j] != -1: return dp[i][j]
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                dp[i][j] = 1 if s[i] == s[j] else 0
            else:
                dp[i][j] = 1 if s[i] == s[j] and search(i+1, j-1) else 0
            return dp[i][j]

        n = len(s)
        dp = [[-1] * n for _ in range(n)]


        for size in range(n, 0, -1):
            i, j = 0, size - 1
            while j < n:
                dp[i][j] = search(i, j)
                if dp[i][j] == 1:
                    return s[i:j+1]
                i += 1
                j += 1
        return ''

    def longestPalindrome_TLE(self, s):
        """
        :type s: str
        :rtype: str
        """
        def search(i, j):
            if dp[i][j] != -1: return dp[i][j]
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                dp[i][j] = 1 if s[i] == s[j] else 0
            else:
                dp[i][j] = 1 if s[i] == s[j] and search(i+1, j-1) else 0
            return dp[i][j]
            
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1, i-1, -1):
                dp[i][j] = search(i, j)
        for size in range(n, 0, -1):
            i, j = 0, size - 1
            while j < n:
                if dp[i][j] == 1: return s[i:j+1]
                i += 1
                j += 1
        return '' 
        
 
    def longestPalindrome_bruteforce(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrom(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        n = len(s)
        for size in range(n, 0, -1):
            for i in range(n - size + 1):
                if is_palindrom(i, i + size - 1):
                    return s[i:i+size]
        return ''
        
    def longestPalindrome_failed(self, s):
        """
        :type s: str
        :rtype: str
        """
        # i = substring length
        # j = substring's start index
        # dp[i][j] =
        # i % 2 != 0
        #   dp[i/2][j] and dp[i/2]...
        if not s: return True
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        dp[0] = [1] * n
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[1][i] = 1
        for i in range(2, n):
            for j in range(n - i):
                pass       
        return ''

    def longestPalindrome_manacher(self, s):
        """
        :type s: str
        :rtype: str
        """
        # https://articles.leetcode.com/longest-palindromic-substring-part-ii/
        # https://algodast.quora.com/Manachar%E2%80%99s-Algorithm
        def preprocess(s):
            if not s: return "^$"
            return "^#" + "#".join(s) + "#$"

        # populated string
        T = preprocess(s)
        # maximum palidrome around T[i]
        P = [0] * len(T)
        # center, right
        C, R = 0, 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * C - i  # i' = C - (i - C)
            P[i] = min(R - i, P[i_mirror]) if R > i else 0
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C = i
                R = i + P[i]
        max_index = 0
        for i in range(1, len(T) - 1):
            if P[i] >  P[max_index]:
                max_index = i
        start = (max_index - 1 - P[max_index]) // 2
        return s[start:start+P[max_index]]
        

if __name__ == '__main__':
    test_cases = [
        ("a", ("a")),
        ("babad", ("bab", "aba")),
        ("cbbd", ("bb")),
        ("abcde", ("a", "b", "c", "d", "e")),
        ("forgeeksskeegfor", ("geeksskeeg")),
        ("abcbabcbabcba", ("abcbabcbabcba")),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().longestPalindrome(test_case[0])
        print('output:', output)
        if test_case[1]:
            assert output
        assert output in test_case[1]

