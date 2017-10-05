#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-03 12:22:18
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island = 0
        for i, row in enumerate(grid):
            for j, column in enumerate(row):
                if grid[i][j] == "1":
                    island += 1
                    self.dfs(grid, i, j)
        return island

    def dfs(self, grid, x, y):
        len_r = len(grid)
        len_c = len(grid[0])
        if x < 0 or y < 0 or x > len_r - 1 or y > len_c - 1:
            return
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)


if __name__ == '__main__':
    s = Solution()
    print s.numIslands([list("11110"),
                        list("11010"),
                        list("11000"),
                        list("00000")])
    print s.numIslands([list("11000"),
                        list("11000"),
                        list("00100"),
                        list("00011")])
