#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-27 22:11:41
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     i = 0
    #     j = 0
    #     x = []
    #     for x in m:
    #         for y in n:
    #             result = []
    #             if self.find_path(i, j, m, n, result):
    #                 x.append(result)
    #     print x

    # def find_path(self, i, j, m, n, result = []):
    #     result.append([i, j])
    #     if i == m and j == n:
    #         return True
    #     if i > m or j > n:
    #         return False
    #     if i + 1 < m:
    #         return self.find_path(i + 1, j, m, n, result)
    #     if j + 1 < n:
    #         return self.find_path(i, j + 1, m, n, result)
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     if m == 1 or n == 1:
    #         return 1
    #     return self.uniquePaths(m -1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            result[i][0] = 1
        for j in range(n):
            result[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[m - 1][n - 1]


if __name__ == '__main__':
    print Solution().uniquePaths(3, 7)
