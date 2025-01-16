#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-16 22:05:09
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/word-pattern
# @Version : $Id$
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_map = defaultdict(list)
        s_list = s.split(" ")
        pattern_length = len(pattern)
        s_list_length = len(s_list)
        # 不相等说明有pattern中的letter对应不上
        if pattern_length != s_list_length:
            return False
        for i, c in enumerate(pattern):
            word_map[c].append(s_list[i])
        # 针对case 4情况，每个letter对应的word必须是唯一的
        unique = set()
        for k, v in word_map.items():
            v_length = len(set(v))
            if v_length != 1:
                return False
            if v[0] in unique:
                return False
            unique.add(v[0])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))
    print(s.wordPattern("abba", "dog cat cat fish"))
    print(s.wordPattern("aaaa", "dog cat cat dog"))
    # case 4
    print(s.wordPattern("abba", "dog dog dog dog"))
