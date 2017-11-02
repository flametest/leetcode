#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-28 16:16:58
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


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


if __name__ == '__main__':
    s = Solution()
    print s.rob([2, 4, 5, 6, 7, 9])
