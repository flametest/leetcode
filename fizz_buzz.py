#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-25 18:03:27
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []

        for x in range(1, n+1):
            t = ""
            if x % 15 ==0:
                t += "FizzBuzz"
            elif x % 3 == 0:
                t += "Fizz"
            elif x % 5 == 0:
                t += "Buzz"
            else:
                t = str(x)

            r.append(t)

        return r


if __name__ == '__main__':
    print Solution().fizzBuzz(15)