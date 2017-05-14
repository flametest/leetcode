#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 08:53:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)
        binary_num = bin_num[2:]
        tmp_list = []
        for i in binary_num:
            if i == "0":
                tmp_list.append("1")
            if i == "1":
                tmp_list.append("0")
        complement_num = "0b" + "".join(tmp_list)
        return int(complement_num, 2)


if __name__ == '__main__':
    print Solution().findComplement(5)
    print Solution().findComplement(0)
    print Solution().findComplement(1)
    print Solution().findComplement(8)
