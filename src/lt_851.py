"""
https://leetcode.com/contest/weekly-contest-88/problems/loud-and-rich/
"""

"""
In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label x, simply "person x".

We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

Also, we'll say quiet[x] = q if person x has quietness q.

Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.

 

Example 1:

Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
There isn't anyone who definitely has more money than person 7, so the person who definitely has
equal to or more money than person 7 is just person 7.

The other answers can be filled out with similar reasoning.

Note:

    1 <= quiet.length = N <= 500
    0 <= quiet[i] < N, all quiet[i] are different.
    0 <= richer.length <= N * (N-1) / 2
    0 <= richer[i][j] < N
    richer[i][0] != richer[i][1]
    richer[i]'s are all different.
    The observations in richer are all logically consistent.
"""

import collections

class Solution:
    def loudAndRich(self, richer, quiet):
        m = collections.defaultdict(list)
        for i, j in richer: m[j].append(i)
        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] >= 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]:
                    res[i] = res[j]
            return res[i]

        for i in range(len(quiet)): dfs(i)
        return res

    def loudAndRich2(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        rank = collections.defaultdict(list)
        for x, y in richer:
            rank[y].append(x)
        # expand
        for x in rank.keys():
            queue = rank[x]
            s = set(queue)
            while queue:
                y = queue.pop()
                s.add(y)
                if y in rank: queue.extend(rank[y])
            rank[x] = list(s)
        print(rank)
        # pick the least quiet person y who has more money than x
        answer = [x for x in range(len(quiet))]
        for i in range(len(answer)):
            print(i, rank[i])
            if len(rank[i]) > 0:
                answer[i] = min(rank[i], key=lambda n: quiet[n]) 
        print(answer)
        return answer
        

if __name__ == '__main__':
    test_cases = [
        (([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]), [5,5,2,5,4,5,6,7]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().loudAndRich(*test_case[0])
        print('output:', output)
        assert output == test_case[1]
