#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-04 20:42:50
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        r = []
        while True:
            nums = self.get_nums(n)
            n = sum([i**2 for i in nums])
            if n == 1:
                return True
            elif n in r:
                return False
            else:
                r.append(n)


    def get_nums(self, m):
        nums = []
        while m:
            nums.append (m % 10)
            m = m / 10
        return nums



if __name__ == '__main__':
    print Solution().isHappy(1)
    print Solution().isHappy(14)
    print Solution().isHappy(19)
    print Solution().isHappy(26)
