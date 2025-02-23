#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-02-23 23:27:36
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/find-and-replace-pattern/
# @Version : $Id$
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res: list[str] = []
        for word in words:
            if match_pattern(word, pattern):
                res.append(word)
        return res


def match_pattern(w1: str, w2: str) -> bool:
    p1 = find_pattern(w1)
    p2 = find_pattern(w2)
    if len(p1) != len(p2):
        return False
    matched: dict[str, str] = {}
    for l1, l2 in zip(w1, w2):
        if p1[l1] != p2[l2]:
            return False
        if l1 in matched:
            if matched[l1] != l2:
                return False
        else:
            matched[l1] = l2
    return True


def find_pattern(w) -> dict[str, int]:
    p: dict[str, int] = {}
    for l in w:
        if l not in p:
            p[l] = 0
        p[l] += 1
    return p


if __name__ == '__main__':
    s = Solution()
    print(s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
    print(s.findAndReplacePattern(["a", "b", "c"], "a"))
    print(s.findAndReplacePattern(["aa", "bb", "ab", "cd"], "aa"))
    print(s.findAndReplacePattern(["abc", "cba", "xyx", "yxx", "yyx"], "abc"))
    print(s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
    print(s.findAndReplacePattern(["badc", "abab", "dddd", "dede", "yyxx"], "baba"))
    # print(find_pattern("abc"))
    # print(match_pattern("mee", "abb"))
