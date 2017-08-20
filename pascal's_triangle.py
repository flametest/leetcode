#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-21 00:23:12
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):

    #  def generate(self, numRows):
    #     """
    #     :type numRows: int
    #     :rtype: List[List[int]]
    #     """
    #     result = []
    #     for i in range(1, numRows + 1):
    #         result.append(self.generate_one(i))
    #     return result

    # def generate_one(self, n):
    #     if n == 1:
    #         return [1]
    #     else:
    #         result = []
    #         for i in range(n):
    #             if i == 0 or i == n - 1:
    #                 result.append(1)
    #             else:
    #                 a = self.generate_one(n - 1)
    #                 result.append(a[i - 1] + a[i])
    #     return result

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows + 1):
            self.generate_one(i, result)
        return result

    def generate_one(self, n, result):
        line = []
        if n == 1:
            line.append(1)
        else:
            for i in range(n):
                if i == 0 or i == n - 1:
                    line.append(1)
                else:
                    # the present maximum index of list result should minus 1,
                    # but we need the previous one, so minus 1 again
                    a = result[n - 1 - 1]
                    line.append(a[i - 1] + a[i])
        result.append(line)


if __name__ == '__main__':
    print Solution().generate(15)
