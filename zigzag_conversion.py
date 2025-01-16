#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2025-01-10 18:47:01
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : https://leetcode.com/problems/zigzag-conversion
# @Version : $Id$

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 先计算需要多少列
        column = 0
        lengthOfStr = len(s)
        flag = True
        # zigzag的中间字符 总是比numRows少2
        # 针对这个case s= "AB"
        minus_row = 2 if numRows > 3 else 0
        while lengthOfStr > 0:
            if flag:
                lengthOfStr -= numRows
                column += 1
                flag = False
            else:
                lengthOfStr -= numRows - minus_row
                column += numRows - minus_row
                flag = True
        # 初始化一个二维数组放置s字符串
        matrix = [[""] * column for _ in range(numRows)]
        # 按照zigzag放置原始字符串
        switch_flag = True
        i = j = k = 0
        while k < len(s) and i < numRows and j < column:
            if switch_flag:
                for x in range(numRows):
                    if i >= numRows or j >= column:
                        break
                    matrix[x][j] = s[k]
                    k += 1
                    i = x
                    if k >= len(s):
                        break
                # 这里在循环外加减
                j += 1
                i -= 1
                switch_flag = False
            else:
                for x in range(numRows - 2):
                    if i >= numRows or j >= column:
                        break
                    matrix[i][j] = s[k]
                    # 这里需要在循环内加减
                    j += 1
                    i -= 1
                    k += 1
                    if k >= len(s):
                        break
                switch_flag = True
        # 按照line by line的顺序读
        res = []
        for a in range(numRows):
            for b in range(column):
                res.append(matrix[a][b])
        return "".join(res)


# https://www.youtube.com/watch?v=Q2Tw6gcVEwc
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                # middle row
                if 0 < r < numRows - 1 and i * increment - 2 * r < len(s):
                    res += s[i * increment - 2 * r]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("A", 1))
    print(s.convert("AB", 1))
    print(s.convert("PAYPALISHIRING", 6))
