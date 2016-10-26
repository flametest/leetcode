#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-25 18:12:54
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
        
if __name__ == '__main__':
    print Solution().canWinNim(6)