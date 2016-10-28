#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 11:54:16
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    print Solution().addDigits(0)
    print Solution().addDigits(39)
