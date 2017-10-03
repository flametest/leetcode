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
        perimeter = 0
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                    if element == 1:
                        perimeter += self.count_edge(grid, i, j)
        return perimeter

    def count_edge(self, grid, i, j):
        edges = 4
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if x not in range(0, len(grid)) or \
                    y not in range(0, len(grid[0])):
                continue
            if grid[x][y] == 1:
                edges -= 1
        return edges


if __name__ == '__main__':
    print Solution().islandPerimeter([[0, 1, 0, 0],
                                      [1, 1, 1, 0],
                                      [0, 1, 0, 0],
                                      [1, 1, 0, 0]])
    print Solution().islandPerimeter([])
