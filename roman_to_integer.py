#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-03 15:08:23
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        for i, l in enumerate(s):
            if 0 <= i < len(s) - 1 and romanMap[l] < romanMap[s[i+1]]:
                    sum -= romanMap[l]
            else:
                sum += romanMap[l]
        return sum

if __name__ == '__main__':
    print Solution().romanToInt("IX")
    print Solution().romanToInt("X")