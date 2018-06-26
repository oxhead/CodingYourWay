"""
https://leetcode.com/contest/weekly-contest-88/problems/maximize-distance-to-closest-person/
"""

"""
849. Maximize Distance to Closest Person

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Easy

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Note:

    1 <= seats.length <= 20000
    seats contains only 0s or 1s, at least one 0, and at least one 1.
"""

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dist_left = [0] * len(seats)
        dist_right = [0] * len(seats)
        left_most = None
        for i, occupied in enumerate(seats):
            if occupied: left_most = i
            if left_most != None:
                dist_left[i] = i - left_most
            else:
                dist_left[i] = None
        right_most = None
        for i, occupied in reversed(list(enumerate(seats))):
            if occupied: right_most = i
            if right_most != None:
                dist_right[i] = right_most - i
            else:
                dist_right[i] = None
        max_dist = 0
        for i in range(len(seats)):
            if dist_left[i] != None and dist_right[i] != None:
                max_dist = max(max_dist, min(dist_left[i], dist_right[i]))
            else:
                max_dist = max(max_dist, dist_left[i] or dist_right[i])
        return max_dist
        

if __name__ == '__main__':
    test_cases = [
        ([1,0,0,0,1,0,1], 2),
        ([1,0,0,0], 3),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().maxDistToClosest(test_case[0])
        print('output:', output)
        assert output == test_case[1]
