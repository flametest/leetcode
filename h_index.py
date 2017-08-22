#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-22 02:22:53
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort(reverse=True)
        i = 0
        max_h = 0
        for i, item in enumerate(citations):
            if item >= len(citations[:i + 1]):
                max_h = len(citations[:i + 1])
        return max_h


if __name__ == '__main__':
    print Solution().hIndex([3, 0, 6, 1, 5])
    print Solution().hIndex([100])
    print Solution().hIndex([100, 99, 1])
    print Solution().hIndex([22, 122, 222])
