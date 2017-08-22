#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 01:14:19
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        i = 0
        while True:
            if i + 1 == len(intervals):
                break
            intervals = self.merge_helper(intervals, i, i + 1)
            i += 1
        return [interval for interval in intervals if interval]

    def merge_helper(self, intervals, i, j):
        if self.is_overlap(intervals[i], intervals[j]):
            # as they have been sorted by attribute start of Interval
            intervals[j].start = intervals[i].start
            # attribute end has not been sorted
            intervals[j].end = max(intervals[j].end, intervals[i].end)
            intervals[i] = 0
        return intervals

    def is_overlap(self, interval1, interval2):
        if set(range(interval1.start, interval1.end + 1))\
                & set(range(interval2.start, interval2.end + 1)):
            return True
        return False


if __name__ == '__main__':
    interval = [Interval(1, 3), Interval(2, 6),
                Interval(8, 10), Interval(15, 18)]
    # print Solution().merge_helper([Interval(1, 3), Interval(2, 6)], 0, 1)
    print Solution().merge(interval)
    interval1 = [Interval(1, 4), Interval(5, 6)]
    print Solution().merge(interval1)
    interval2 = [Interval(1, 4), Interval(4, 6)]
    print Solution().merge(interval2)
    interval3 = [Interval(1, 4), Interval(2, 3)]
    print Solution().merge(interval3)
