#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 10:46:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        length = len(candies)
        kinds = len(set(candies))
        return kinds if kinds < length / 2 else length / 2


if __name__ == '__main__':
    print Solution().distributeCandies([1, 1, 2, 2, 3, 3])
    print Solution().distributeCandies([1, 1, 2, 3])
    print Solution().distributeCandies([1, 1])
    print Solution().distributeCandies([1, 2])
    print Solution().distributeCandies([])
