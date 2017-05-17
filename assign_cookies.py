#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-17 11:33:01
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        sa = 0
        g.sort()
        s.sort()
        for gi in g:
            for si in s:
                if si >= gi:
                    sa += 1
                    s.remove(si)
                    break
        return sa


if __name__ == '__main__':
    print Solution().findContentChildren([1, 2, 3], [1, 1])
    print Solution().findContentChildren([1, 2], [1, 2, 3])
    print Solution().findContentChildren([3, 4], [1, 2])
