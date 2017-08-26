#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-26 23:55:43
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        tmp = []
        for str in strs:
            tmp.append(list(str))
        for i in zip(*tmp):
            if not i:
                break
            if len(set(i)) != 1:
                break
            result += i[0]
        return result


if __name__ == '__main__':
    print Solution().longestCommonPrefix([""])
    print Solution().longestCommonPrefix(["a"])
    print Solution().longestCommonPrefix(["axb", "aac", "aad"])
