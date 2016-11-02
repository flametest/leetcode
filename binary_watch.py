#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-02 16:32:53
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        import itertools
        HOURS = [1, 2, 4, 8]
        MINUTES = [1, 2, 4, 8, 16, 32]
        sum_list = self.get_sum_list(num)
        r = []
        for h, m in sum_list:
            hours = [sum(i) for i in itertools.combinations(HOURS, h) if sum(i) < 12]
            minutes = [sum(j) for j in itertools.combinations(MINUTES, m) if sum(j) <= 59]
            for k,l in itertools.product(hours, minutes):
                r.append("%d:%02d"%(k,l)) 
        return r

    def get_sum_list(self, num):
        r = []
        for i in range(num+1):
            if i <= 4 and num - i <= 6:
                r.append((i, num - i))
        return r


if __name__ == '__main__':
    print Solution().get_sum_list(4)
    print Solution().readBinaryWatch(0)
    print Solution().readBinaryWatch(1)
    print Solution().readBinaryWatch(2)
