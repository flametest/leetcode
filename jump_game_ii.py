#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-08 15:51:14
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/jump-game-ii
# @Version : $Id$
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        if goal == 0:
            return 0
        path_list = []
        i = 0
        while i < goal:
            path_list.append(nums[i])
            step = nums[i]
            max_reachable = i + step
            next_idx = i
            if max_reachable >= goal:
                break
            for j in range(i, min(i + step + 1, len(nums))):
                if j + nums[j] > max_reachable:
                    next_idx = j
                    max_reachable = j + nums[j]
            if max_reachable >= goal:
                path_list.append(nums[next_idx])
                break
            i = next_idx

        return len(path_list)


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]) == 2)
    print(s.jump([2, 3, 0, 1, 4]) == 2)
    print(s.jump([2, 3, 1]) == 1)
    print(s.jump([2, 1]) == 1)
    print(s.jump([0]) == 0)
    print(s.jump([1, 2, 3, 4]) == 2)
    print(s.jump([1]) == 0)
    print(s.jump([1, 2]) == 1)
    print(s.jump([1, 2, 3, 4, 5]) == 3)
    print(s.jump([3, 4, 3, 2, 5, 4, 3]) == 3)
