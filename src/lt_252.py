"""
https://leetcode.com/problems/meeting-rooms
https://leetcode.com/problems/meeting-rooms-ii

Related:
  - lt_56_merge-intervals
  - lt_253_meeting-rooms-ii

"""

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""

from base import Interval

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # Time: O(nlogn)
        # Space: O(1)
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

if __name__ == '__main__':
    test_cases = [
        ([[0, 10]], True),
        ([[0, 10], [20, 30]], True),
        ([[0, 30],[5, 10],[15, 20]], False),
        ([[0, 10], [5, 35], [15, 20], [25, 40]], False),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().canAttendMeetings([Interval(*interval) for interval in test_case[0]])
        print('output:', output)
        assert output == test_case[1]

