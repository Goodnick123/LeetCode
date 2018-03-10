# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 13:14
# @Author  : Yeh

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        flags =[[False]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.wfs(board,flags,word,i,j,0)==True:
                    return True
        return False
    def wfs(self,board,flags,word,i,j,index):
        if index == len(word): return True
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or flags[i][j] == True or word[index] !=board[i][j]:
            return False
        flags[i][j] =True
        flag =self.wfs(board,flags,word,i-1,j,index+1) or self.wfs(board,flags,word,i+1,j,index+1) or self.wfs(board,flags,word,i,j-1,index+1) or self.wfs(board,flags,word,i,j+1,index+1)
        flags[i][j]=False
        return flag




demo  = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word="ABCB"
print(demo.exist(board,word))