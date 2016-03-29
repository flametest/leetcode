#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-29 12:06:01
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        tmp_list = []
        tag = ""
        str_list = list(str(x))
        for i in str_list:
            if i.isdigit():
                tmp_list.insert(0, i)
            else:
                tag = i
        tmp_list.insert(0, tag)
        result = int("".join(tmp_list))
        # import sys
        # if result > sys.maxint-1 or result < -sys.maxint - 1:
        #     return 0
        if result > 2**31 -1 or result < -2**31 - 1:
            return 0
        return result



if __name__ == '__main__':
    a = 1534236469
    print Solution().reverse(a)

