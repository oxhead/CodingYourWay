"""
https://leetcode.com/problems/palindrome-partitioning

Related:
  - lt_132_palindrome-partitioning-ii
"""

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Time: O(?)
        # Space: O(n)
        # Hints:
        # 1) backtracking (s -> s1s2
        # 2) if s2 if palindrom, current + [s2]
        # 3) keep splitting s2
        def is_palindrome(ps):
            return ps == ps[::-1]

        def search(left, right, current):
            if is_palindrome(s[left:right]):
                output.append(current + [s[left:right]])
            for i in range(left + 1, right):
                s1 = s[left:i]
                if not is_palindrome(s1):
                    continue
                current.append(s1)
                search(i, right, current)
                current.pop()
             
        output = []
        search(0, len(s), [])
        return output

    def partition_cached(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def search(start, end, current):
            r = s[start:end]
            if r in records or r == r[::-1]:
                output.append(current + [r])
            for i in range(start + 1, end):
                r = s[start:i]
                if r not in records and r != r[::-1]: continue
                records.add(r)
                current.append(r)
                search(i, end, current)
                current.pop() 
        records = set()
        output = []
        search(0, len(s), [])
        return output 


if __name__ == '__main__':
    test_cases = [
        ("aab", [["a","a","b"], ["aa","b"]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().partition(test_case[0])
        print('output:', output)
        assert output == test_case[1]

