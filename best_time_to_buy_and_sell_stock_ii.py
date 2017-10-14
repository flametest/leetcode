#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-13 11:10:26
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit_max = 0
        length = len(prices)
        k = 0
        j = k + 1
        profit_sum = 0
        while k < j < length:
            if prices[j] > prices[k]:
                profit = prices[j] - prices[k]
                profit_sum += profit
                k = j
                j = k + 1
                continue
            else:
                k = j
            j += 1
        if profit_sum > profit_max:
            profit_max = profit_sum
        return profit_max      


if __name__ == '__main__':
    s = Solution()
    # print s.maxProfit([])
    # print s.maxProfit([4])
    print s.maxProfit([7, 1, 5, 3, 6, 4])
    print s.maxProfit([7, 1, 3, 2, 8, 4])
    print s.maxProfit([1, 2, 4])
