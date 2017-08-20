#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-19 12:22:13
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        position = []
        solutions = self.solve_helper(n, position)
        return self.pprint(solutions)

    def pprint(self, solutions):
        results = []
        for solution in solutions:
            result = []
            for i in solution:
                result.append("." * i + "Q" + "." * (len(solution) - i - 1))
            results.append(result)
        return results

    def solve_helper(self, n, position):

        for j in range(n):
            if not self.conflict(position, j):
                if len(position) == n - 1:
                    yield [j]
                else:
                    for result in self.solve_helper(n, position + [j]):
                        yield [j] + result

    def conflict(self, position, row_index):
        cols = len(position)
        for col in range(cols):
            if row_index == position[col] or \
               abs(position[col] - row_index) == (cols - col):
                return True
        else:
            return False


if __name__ == '__main__':
    print Solution().solveNQueens(4)
    print Solution().solveNQueens(8)
