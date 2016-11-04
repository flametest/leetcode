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
        return str(self.get_int(num1) + self.get_int(num2))

    def get_int(self, s_num):
        sum = 0
        for k, i in enumerate(reversed(s_num)):
            sum += (ord(i) - ord("0")) * 10 ** k
        return sum



if __name__ == '__main__':
    print Solution().get_int("89")
    print Solution().addStrings("8", "9")
