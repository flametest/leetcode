#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 17:02:59
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        result = []
        for i in range(1, int(math.ceil(math.sqrt(area))) + 1):
            if area % i == 0:
                j = area / i
                result.append((j, i))
        min_index = None
        min_diff = float("inf")
        for k, (l, w) in enumerate(result):
            if l < w:
                continue
            if l - w < min_diff:
                min_diff = l - w
                min_index = k
        if min_index is not None:
            return result[min_index]


if __name__ == '__main__':
    print Solution().constructRectangle(4)
    print Solution().constructRectangle(2)
    print Solution().constructRectangle(15)
