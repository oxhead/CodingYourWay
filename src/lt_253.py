"""
https://leetcode.com/problems/meeting-rooms-ii

Related:
  - lt_56_merge-intervals
  - lt_252_meeting-rooms
  - lt_452_minimum-number-of-arrows-to-burst-balloons
"""

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

import heapq
import operator

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Time: O(nlogn)
        # Space: O(n)
        # scanline or sweep line algotihm?
        count = 0
        heap = []
        intervals.sort(key=operator.attrgetter('start'))
        for interval in intervals:
            heapq.heappush(heap, interval.end)
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            count = max(count, len(heap))
        return count

    def minMeetingRooms_sort(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Time: O(nlogn)
        # Space: O(n)
        # http://www.cnblogs.com/yrbbest/p/5012534.html
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals]) 
        count = 0
        end_index = 0
        print('start:', starts)
        print('end:', ends) 
        for i in range(len(intervals)):
            if starts[i] < ends[end_index]: count += 1
            else: end_index += 1
        return count

    def minMeetingRooms_map(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Time: O(nlogn)
        # Space: O(n)
        # http://blog.csdn.net/qq508618087/article/details/50762939
        records = {}
        for interval in intervals:
            if interval.start not in records: records[interval.start] = 0
            records[interval.start] += 1
            if interval.end not in records: records[interval.end] = 0
            records[interval.end] -= 1
        ans = count = 0
        for k in sorted(records.keys()):
            count += records[k]
            ans = max(ans, count)
        return ans


if __name__ == '__main__':
    test_cases = [
        ([], 0),
        ([[0, 30],[5, 10],[15, 20]], 2),
        ([[0, 10], [5, 35], [15, 20], [25, 40]], 2),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        output = Solution().minMeetingRooms([Interval(*interval) for interval in test_case[0]])
        print('output:', output)
        assert output == test_case[1]

