"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target

Related:
"""

"""
 Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:

    letters has a length in range [2, 10000].
    letters consists of lowercase letters, and contains at least 2 unique letters.
    target is a lowercase letter.
"""

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Time: O(logn)
        # Space: O(1)
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target: left = mid + 1
            else: right = mid - 1
        return letters[left] if left < len(letters) else letters[0]

       
if __name__ == '__main__':
    test_cases = [
        ((["c", "f", "j"], "a"), "c"),
        ((["c", "f", "j"], "c"), "f"),
        ((["c", "f", "j"], "d"), "f"),
        ((["c", "f", "j"], "g"), "j"),
        ((["c", "f", "j"], "j"), "c"),
        ((["c", "f", "j"], "k"), "c"),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().nextGreatestLetter(*test_case[0])
        print('output:', output)
        assert output == test_case[1]

