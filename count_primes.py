#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 16:25:32
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


# class Solution(object):
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         num_of_primes = 0
#         for i in xrange(n):
#             if self.is_prime(i):
#                 num_of_primes += 1
#         return num_of_primes

#     def is_prime(self, num):
#         if num <= 1:
#             return False
#         from math import sqrt
#         for i in range(2, int(sqrt(num) + 1)):
#             if num % i == 0 and num != i:
#                 return False
#         return True
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        prime = [1] * n
        prime [0] = prime[1] = 0
        i = 2
        from math import sqrt
        while i < sqrt(n):
            if not prime[i]:
                i = i + 1
                continue
            for j in range(i * i, n, i):
                prime[j] = 0
            i = i + 1
        return sum(prime)


if __name__ == '__main__':
    print Solution().countPrimes(1)
    print Solution().countPrimes(3)
    print Solution().countPrimes(100)
    print Solution().countPrimes(999983)
