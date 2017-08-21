#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-22 00:11:37
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(gas)):
            if self.cal_tank(gas, cost, i) >= 0:
                return i
        else:
            return -1

    def cal_tank(self, gas, cost, start):
        tank = 0
        for _ in range(len(gas)):
            tank += gas[start]
            tank -= cost[start]
            if tank < 0:
                return tank
            if start < len(gas) - 1:
                start += 1
            else:
                start = start - len(gas) + 1
        return tank


if __name__ == '__main__':
    print Solution().canCompleteCircuit([1, 2, 3], [1, 2, 3])
    print Solution().canCompleteCircuit([1, 2], [2, 1])
    