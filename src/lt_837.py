"""
https://leetcode.com/problems/new-21-game
"""

"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.

Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.

Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278

Note:

    0 <= K <= N <= 10000
    1 <= W <= 10000
    Answers will be accepted as correct if they are within 10^-5 of the correct answer.
    The judging time limit has been reduced for this question.
"""

class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0: return 1
        dp = [1.0] + [0.0] * N
        W_sum = 1.0
        for i in range(1, N + 1):
            dp[i] = W_sum / W
            if i < K: W_sum += dp[i]
            if 0 <= i - W < K: W_sum -= dp[i - W]
        return sum(dp[K:])


    def new21Game_failed(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        def calculate(n, k, w):
            if (n, k) in records: return records[(n, k)]
            elif k == 1: return (n, w)
            for i in range(k):
                possible, total = calculate(n - 1, k - 1, w)
            records[(n - 1, k - 1)] = (possible, total)
            return (possible + 1, total + w)
        records = {}
        result = calculate(N, K, W)
        return result[0] / result[1]
         
        
if __name__ == '__main__':
    test_cases = [
        ((10, 1, 10), 1.0),
        ((6, 1, 10), 0.6),
        ((21, 17, 10), 0.73278),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().new21Game(*test_case[0])
        print('output:', output)
        assert abs(output - test_case[1]) < 0.00001
