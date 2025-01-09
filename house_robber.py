#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-28 16:16:58
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
from typing import List


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        not_rob = 0
        rob = 0
        for num in nums:
            curr_rob = not_rob + num
            not_rob = max(not_rob, rob)
            rob = curr_rob
        return max(rob, not_rob)


class Solution1(object):
    def rob(self, nums: List[int]) -> int:
        rob = 0
        not_rob = 0
        for num in nums:
            temp = rob
            # 如果选择抢当前这家，那么更新rob，在此之前先保存rob
            rob = max(not_rob + num, rob)
            # 如果选择不抢这家，那么更新not_rob位之前的rob
            not_rob = temp
        return rob


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 4, 5, 6, 7, 9]))
    s1 = Solution1()
    print(s.rob([2, 4, 5, 6, 7, 9]))
