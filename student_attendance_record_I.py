#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-29 13:26:29
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_num = s.count("A")
        l_num = s.count("L")
        if a_num > 1 or l_num > 2:
            return False
        return True


if __name__ == '__main__':
    print Solution().checkRecord("PPALLP")
    print Solution().checkRecord("PPALLL")
