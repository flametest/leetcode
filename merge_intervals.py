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
        result = []
        vals = []
        for interval in intervals:
            vals.append(interval.start)
            vals.append(interval.end)
        vals.sort()
        row = [0] * (max(vals) + 1)
        for interval in intervals:
            for i in range(interval.start, interval.end + 1):
                row[i] = 1
        interval_index = []
        for i, j in enumerate(row):
            if j == 1:
                interval_index.append(i)
            if j == 0 or i == len(row) - 1:
                if interval_index:
                    result.append(Interval(interval_index[0],
                                           interval_index[-1]))
                interval_index = []
        return result


if __name__ == '__main__':
    interval = [Interval(1, 3), Interval(2, 6),
                Interval(8, 10), Interval(15, 18)]
    print Solution().merge(interval)
