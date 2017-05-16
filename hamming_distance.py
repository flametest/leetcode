#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 17:33:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        hamming_distance = 0
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        import itertools
        for i, j in itertools.izip_longest(reversed(bin_x),
                                           reversed(bin_y), fillvalue='0'):
            if i != j:
                hamming_distance += 1
        return hamming_distance


if __name__ == '__main__':
    print Solution().hammingDistance(5, 6)
    print Solution().hammingDistance(1, 4)
