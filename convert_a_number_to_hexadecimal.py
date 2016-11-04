#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-04 15:50:38
# @Author  : jun.jiang (flametest@gmail.com)
# @Link    : http://www.qunar.com
# @Version : $Id$

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        MASK = 0xFFFFFFFF
        
        if num == 0:
            return "0"
        if num < 0:
            num = ~ (num ^ MASK) # if num < 0: num += 2**32
        h_mapping = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        mapping = {i:i for i in range(10)}
        mapping.update(h_mapping)
        r = []
        while num:
            t = num % 16
            num = num / 16
            r.append(mapping[t])
            if 0 < num < 16:
                r.append(mapping[num])
                break
        return ''.join([str(i) for i in reversed(r)])

if __name__ == '__main__':
    print Solution().toHex(0)
    print Solution().toHex(26)
    print Solution().toHex(-26) #"ffffffe6"
    print Solution().toHex(1000)
    print Solution().toHex(-1)
    print Solution().toHex(1)
