#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-04 15:25:04
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))

if __name__ == '__main__':
    print Solution().addStrings("8", "9")
