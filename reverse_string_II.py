#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-29 14:15:39
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = []
        start = 0
        while True:
            if len(s[start:]) < k:
                result.append(s[start:][::-1])
                break
            if k < len(s[start:]) < 2 * k:
                result.append(s[start:(start + k)][::-1] + s[start + k:])
                break
            tmp = s[start:(start + 2 * k)]
            result.append(tmp[:2][::-1] + tmp[2:])
            start += 2 * k
        return "".join(result)


if __name__ == '__main__':
    print Solution().reverseStr("abcdefg", 2)
