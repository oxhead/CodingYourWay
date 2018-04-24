"""
https://leetcode.com/problems/merge-intervals

Related:
  - lt_57_insert-interval
  - lt_252_meeting-rooms
  - lt_253_meeting-rooms-ii
  - lt_495_teemo-attacking
  - lt_616_add-bold-tag-in-string
  - lt_715_range-module
  - lt_759_employee-free-time
  - lt_763_partition-labels
"""

"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

from base import Interval
from utils import to_interval_list, is_interval_equal

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Time: O(nlogn)
        # Space: O(1)
        if not intervals: return []
        intervals.sort(key=lambda x: x.start)
        output = []
        current_interval = Interval(intervals[0].start, intervals[0].end)
        for interval in intervals[1:]:
            if interval.start > current_interval.end:
                output.append(current_interval)
                current_interval = Interval(interval.start, interval.end)
            else:
                current_interval.end = max(current_interval.end, interval.end)
        output.append(current_interval)
        return output

    def merge_verbose(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Time: O(nlogn)
        # Space: O(1)
        if not intervals: return []
        elif len(intervals) == 1: return intervals

        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        left = 0
        output = []
        while left < len(intervals):
            right = left + 1
            interval = Interval(intervals[left].start, intervals[left].end)
            while right < len(intervals):
                if intervals[right].start > interval.end:
                    break
                if intervals[right].start < interval.start:
                    interval.start = intervals[right].start
                if intervals[right].end > interval.end:
                    interval.end = intervals[right].end
                left = right
                right += 1
            output.append(interval)
            left = right
        return output


if __name__ == '__main__':
    test_cases = [
        ([], []),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
    ]

    for test_case in test_cases:
        print('case:', test_case)
        intervals = to_interval_list(test_case[0])
        output = Solution().merge(intervals)
        print('output:', [(o.start, o.end) for o in output])
        assert is_interval_equal(output, to_interval_list(test_case[1]))

