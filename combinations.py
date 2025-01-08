#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-08 21:57:15
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/combinations
# @Version : $Id$
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        t = [i for i in range(1, n + 1)]
        results = []
        return self.helper(k, [], t, results)

    def helper(self, l, prev, curr, results) -> List[List[int]]:
        if len(prev) == l:
            results.append(prev)
            return results
        for i, c in enumerate(curr):
            self.helper(l, prev + [c], curr[i + 1:], results)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(1, 1))
