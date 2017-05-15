#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 09:45:14
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land_cell = 0
        perimeter = 0
        # print grid[-1][-1]
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                    if element == 1:
                        land_cell += 1
                        perimeter += self.count_zero(grid, i, j)
        return perimeter

    def count_zero(self, grid, i, j):
        import itertools
        zero_nums = 0
        for x, y in itertools.product([i, i - 1, i + 1], [j, j - 1, j + 1]):
            if x not in range(0, len(grid)) or \
                    y not in range(0, len(grid[0])):
                continue
            if x != i and y != j:
                continue
            if grid[x][y] == 0:
                zero_nums += 1
        if i == 0 or i == len(grid) - 1:
            zero_nums += 1
        if j == 0 or j == len(grid[0]) - 1:
            zero_nums += 1
        return zero_nums


if __name__ == '__main__':
    print Solution().islandPerimeter([[0, 1, 0, 0],
                                      [1, 1, 1, 0],
                                      [0, 1, 0, 0],
                                      [1, 1, 0, 0]])
    print Solution().islandPerimeter([])
