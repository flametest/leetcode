#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-02 16:21:44
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = "1"
        while n - 1:  
            i = self.say(i)
            n -= 1
        return i
    
    def say(self, num):
        result = []
        t = {}
        for s in str(num):
            if t and s in t:
                t[s] += 1
            elif t and s not in t:
                result.append(t)
                t = {}
                t[s] = 1
            elif not t:
                t[s] = 1
        else:
            result.append(t)
        str_res = ""
        for d in result:
            str_res += str(d.values()[0]) + str(d.keys()[0])
        return str_res
            
                
if __name__ == "__main__":
    print Solution().say(1)
    print Solution().say(11)
    print Solution().say(112)
    print Solution().say(1122)
    print Solution().say(11223)
    print Solution().countAndSay(1)
    print Solution().countAndSay(4)
