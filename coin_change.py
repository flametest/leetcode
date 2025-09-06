# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 09:55:15
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
from typing import List


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [amount + 1] * amount
        for i in range(1, len(dp)):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return [dp[amount], -1][dp[amount] == amount + 1]


if __name__ == '__main__':
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([], 11))
    print(Solution().coinChange([1, 2, 5], 0))
    print(Solution().coinChange([2], 1))
    print(Solution().coinChange([186, 419, 83, 408], 6249))
    print("--------")
