"""
https://leetcode.com/problems/palindrome-permutation-ii

Related:
  - lt_31_next-permutation
  - lt_47_permutations-ii
  - lt_266_palindrome-permutation
"""

"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].
"""

import collections

class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # https://leetcode.com/problems/palindrome-permutation-ii/discuss/69700/Python-solution-sharing:-Preprocess-then-it-would-be-like-ordinary-backtracking-permutation!
        def generate(candidates, start, mid, output):
            if start == len(candidates):
                output.append(candidates + mid + candidates[::-1])
                return
            for i in range(start, len(candidates)):
                if i > start and (candidates[i] == candidates[i - 1] or candidates[i] == candidates[start]):
                    continue
                if i == start:
                    permutations = candidates
                else:
                    permutations = candidates[:start] + candidates[i] + candidates[start+1:i] + candidates[start] + candidates[i+1:]
                generate(permutations, start + 1, mid, output)
        counter = collections.Counter(s)
        output = []
        mid = ''.join([k for k, v in counter.items() if v % 2])
        candidates = ''.join([k * (v // 2) for k, v in counter.items()])
        if len(mid) >= 2: return []
        generate(candidates, 0, mid, output) 
        return output
            
        
    def generatePalindromes_TLE_2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # failed to pass "aaaaaaaaaaaaaaaaaaaaaaa"
        def generate_permutations(mid, chars):
            print('mid={}, chars={}'.format(mid, chars))
            output = []
            used = [False] * len(chars) 
            generate(mid, output, used, [], chars)
            return output

        def generate(mid, output, used, current, chars):
            if len(current) == len(chars):
                output.append(''.join(current) + mid + ''.join(current[::-1]))
                return
            for i in range(len(chars)):
                if not used[i] and not (i > 0 and chars[i-1] == chars[i] and used[i - 1]):
                    print('#', i)
                    used[i] = True
                    current.append(chars[i])
                    generate(mid, output, used, current, chars)
                    current.pop()
                    used[i] = False
        count = collections.Counter(s)
        mid = ''.join(k for k, v in count.items() if v % 2)
        chars = ''.join(k * (v // 2) for k, v in count.items()) 
        return generate_permutations(mid, chars) if len(mid) < 2 else []

    def generatePalindromes_TLE_1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def generate(s, current, output):
            if not s:
                output.append(current)
            for i, c in enumerate(s):
                if i - 1 >= 0 and s[i - 1] == c:
                    continue
                generate(s[:i] + s[i+1:], c + current, output)
            
        s = ''.join(sorted(s))
        output = []
        generate(s, "", output)
        return [s for s in output if s == s[::-1]]
        

if __name__ == '__main__':
    test_cases = [
        ("aabb", ["abba", "baab"]),
        ("abc", []),
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"])
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().generatePalindromes(test_case[0])
        print('output:', output)
        assert sorted(output) == sorted(test_case[1])

