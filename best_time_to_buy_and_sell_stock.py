#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-13 10:58:15
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = float("inf")
        max_prof = 0
        for price in prices:
            if price <= min_val:
                min_val = price
            profit = price - min_val
            if profit >= max_prof:
                max_prof = profit
        return max_prof


if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([7, 1, 5, 3, 6, 4])
    print s.maxProfit([7, 6, 4, 3, 1])
    print s.maxProfit([])
    print s.maxProfit([5])