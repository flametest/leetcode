#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-24 00:55:17
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        num = 0
        result = 0
        sign = ""
        if numerator / denominator < 0:
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        m = {}
        repeat_range = []
        while True:
            reminder = numerator % denominator
            quotient = numerator / denominator
            result = result * 10 + quotient
            if reminder == 0:
                break
            numerator = reminder * 10
            if num > denominator:
                break
            if reminder not in m:
                m[reminder] = num
            else:
                repeat_range = [m[reminder], num]
                break
            num += 1
        return sign + self.reformat(result, denominator, num, repeat_range)

    def reformat(self, result, denominator, num, repeat_range):
        from decimal import Decimal
        res = Decimal(result) / 10 ** num
        if res == int(res):
            return str(int(res))
        if not repeat_range:
            return "{:f}".format(res)
        start = repeat_range[0]
        end = repeat_range[1]
        len_str = len(str(result))
        if num >= len_str:
            str_result = "0"*(num - len_str) + str(result)
            return "0."  + str_result[:start] + "(" +\
                str_result[start:end] + ")"
        else:
            decimal_part = str(result)[len_str-num:len_str]
            integer_part = str(result)[:len_str-num]
            str_result = integer_part + "." + decimal_part[:start] + "(" +\
                decimal_part[start:end] + ")"
            return str_result
        
        
       


if __name__ == '__main__':
    print Solution().fractionToDecimal(0, 1)
    print Solution().fractionToDecimal(1, 2)
    print Solution().fractionToDecimal(2, 1)
    print Solution().fractionToDecimal(1, 3)
    print Solution().fractionToDecimal(4, 15)
    print Solution().fractionToDecimal(7, 17)
    print Solution().fractionToDecimal(1, 214748364)
    print Solution().fractionToDecimal(-7, 17)
    print Solution().fractionToDecimal(1, 90)
    print Solution().fractionToDecimal(22, 7)
    print Solution().fractionToDecimal(-1, -2147483648)
