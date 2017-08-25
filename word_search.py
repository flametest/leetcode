#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-25 21:59:08
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if word[0] == item:
                    if self.search(i, j, board, word):
                        return True
        return False

    def search(self, i, j, board, word):
        if word[0] == board[i][j]:
            board[i][j] = "*"
            if len(word[1:]) == 0:
                return True
            if i > 0 and self.search(i-1, j, board, word[1:]):
                return True
            if j > 0 and self.search(i, j-1, board, word[1:]):
                return True
            if i < len(board)-1 and self.search(i+1, j, board, word[1:]):
                return True
            if j < len(board[0])-1 and self.search(i, j+1, board, word[1:]):
                return True
            board[i][j] = word[0]
            return False
        return False



if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print Solution().exist(board, word)
