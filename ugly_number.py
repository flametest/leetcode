#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-24 12:07:37
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        import math
        prime_factors = set()
        for i in range(2, int(math.ceil(math.sqrt(num))) + 1):
            if num % i == 0 and self.isPrime(i):
                prime_factors.add(i)
                if self.isPrime(num / i):
                    prime_factors.add(num / i)
        for p in prime_factors:
            if p not in [2, 3, 5]:
                return False
        else:
            return True

    def isPrime(self, num):
        import math
        if num == 1:
            return True
        for i in range(2, int(math.ceil(math.sqrt(num))) + 1):
            if num % i == 0 and num != i:
                return False
        else:
            return True


if __name__ == '__main__':
    # print Solution().isPrime(2)
    # print Solution().isPrime(1)
    # print Solution().isPrime(4)
    # print Solution().isPrime(7)
    print Solution().isUgly(1)
    print Solution().isUgly(6)
    print Solution().isUgly(8)
    print Solution().isUgly(9)
    print Solution().isUgly(21)
    print Solution().isUgly(14)
