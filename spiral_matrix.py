#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-09 16:39:54
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/spiral-matrix/
# @Version : $Id$
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        if len(matrix) == 0:
            return results
        start_boundary_x = 0
        start_boundary_y = 0

        end_boundary_x = len(matrix) - 1
        end_boundary_y = len(matrix[0]) - 1

        while start_boundary_y <= end_boundary_y and start_boundary_x <= end_boundary_x:
            flip_x_flag = False
            flip_y_flag = False
            for j in range(start_boundary_y, end_boundary_y + 1):
                results.append(matrix[start_boundary_x][j])
            start_boundary_x += 1
            flip_y_flag = True
            for i in range(start_boundary_x, end_boundary_x + 1):
                results.append(matrix[i][end_boundary_y])
            end_boundary_y -= 1
            flip_x_flag = True
            if flip_y_flag and flip_x_flag and (
                    start_boundary_y <= end_boundary_y and start_boundary_x <= end_boundary_x):
                for a in range(end_boundary_y, start_boundary_y - 1, -1):
                    results.append(matrix[end_boundary_x][a])
                end_boundary_x -= 1
                for b in range(end_boundary_x, start_boundary_x - 1, -1):
                    results.append(matrix[b][start_boundary_y])
                start_boundary_y += 1

        return results


if __name__ == '__main__':
    s = Solution()
    # print(s.spiralOrder([
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]]))
    print(s.spiralOrder(
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]))
