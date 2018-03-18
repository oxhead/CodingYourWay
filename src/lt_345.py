"""
https://leetcode.com/problems/reverse-vowels-of-a-string

Related:
  - lt_344_reverse-string
"""

"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y". 
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Time: O(n)
        # Space: O(n)
        if not s: return ""

        output = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        left, right = 0, len(output) - 1
        while left < right:
            left_is_vowel = output[left] in vowels
            right_is_vowel = output[right] in vowels
            if left_is_vowel and right_is_vowel:
                output[left], output[right] = output[right], output[left]
                left += 1
                right -= 1
            elif not left_is_vowel:
                left += 1
            elif not right_is_vowel:
                right -= 1
        return "".join(output)


if __name__ == '__main__':
    test_cases = [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().reverseVowels(test_case[0])
        print('output:', output)
        assert output == test_case[1]

