#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-18
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        sign = ""
        result = []
        if num < 0:
            sign = "-"
            num = -num
        while True:
            a = num % 7
            result.append(str(a))
            num = num / 7
            if num == 0:
                break
        return sign + "".join(result[::-1])


if __name__ == '__main__':
    print Solution().convertToBase7(-7)
    print Solution().convertToBase7(100)
    print Solution().convertToBase7(0)
