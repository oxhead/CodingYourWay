"""
https://leetcode.com/problems/split-array-into-fibonacci-sequence
"""

"""
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

    0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
    F.length >= 3;
    and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]

Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]

Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.

Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.

Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.

Note:

    1 <= S.length <= 200
    S contains only digits.
"""

class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def check_fib(s1, s2, s3):
            if len(s3) < 1: return []
            if len(s1) > 1 and s1[0] == '0': return []
            if len(s2) > 1 and s2[0] == '0': return []
            if int(s1) > 2147483647: return []
            if int(s2) > 2147483647: return []
            if int(s1) + int(s2) == int(s3):
                if len(s3) > 1 and s3[0] == '0': pass
                elif int(s3) > 2147483647: pass
                else:
                    return [int(s1), int(s2), int(s3)]
            for i in range(1, len(s3)):
                if len(s3[:i]) > 1 and s3[:i][0] == '0': continue
                if int(s3[:i]) > 2147483647: continue
                if int(s1) + int(s2) == int(s3[:i]):
                    result = check_fib(s2, s3[:i], s3[i:])
                    if result: return [int(s1)] + result 
            return []

        for i in range(1, len(S)-2):
            for j in range(i + 1, len(S) - 1):
                result = check_fib(S[:i], S[i:j], S[j:])
                if result: return result
        return []
        

if __name__ == '__main__':
    test_cases = [
        ("123456579", ([123,456,579],)),
        ("11235813", ([1,1,2,3,5,8,13],)),
        ("112358130", ([],)),
        ("0123", ([],)),
        ("1101111", ([110, 1, 111], [11, 0, 11, 11])),
        ("1011", ([1, 0, 1, 1],)),
        ("0000", ([0, 0, 0, 0],)),
        ("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511", ([],)),
        ("01123581321345589", ([0,1,1,2,3,5,8,13,21,34,55,89],)),
        ("3611537383985343591834441270352104793375145479938855071433500231900737525076071514982402115895535257195564161509167334647108949738176284385285234123461518508746752631120827113919550237703163294909", ([],)),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().splitIntoFibonacci(test_case[0])
        print('output:', output)
        #print(test_case[0)
        #print("".join([str(n) for n in output]))
        assert output in test_case[1]
