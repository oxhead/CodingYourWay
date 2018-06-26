"""
https://leetcode.com/contest/weekly-contest-88/problems/shifting-letters
"""

"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.

Note:

    1 <= S.length = shifts.length <= 20000
    0 <= shifts[i] <= 10 ^ 9
"""

class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        # https://leetcode.com/problems/shifting-letters/discuss/137906/C++JavaPython-Easy-Understood
        for i in range(len(shifts) - 1)[::-1]: shifts[i] += shifts[i + 1]
        return ''.join([chr((ord(c) - 97 + s) % 26 + 97) for c, s in zip(S, shifts)])

    def shiftingLetters_TLE(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = [ord(c) for c in S]
        for i, shift in enumerate(shifts):
            for j in range(i+1):
                s[j] += shift % 26
        return ''.join([chr((n-97)%26 + 97) for n in s])

if __name__ == '__main__':
    test_cases = [
        (("abc", [3,5,9]), "rpl"),
        (("mkgfzkkuxownxvfvxasy", [505870226,437526072,266740649,224336793,532917782,311122363,567754492,595798950,81520022,684110326,137742843,275267355,856903962,148291585,919054234,467541837,622939912,116899933,983296461,536563513]), 'wqqwlcjnkphhsyvrkdod'),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().shiftingLetters(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
