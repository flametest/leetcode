#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-25 17:56:47
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(list(s)[::-1])


if __name__ == '__main__':
    print Solution().reverseString("hello")