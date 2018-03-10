# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 22:26
# @Author  : Yeh

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # maxCnt = 0
        # if matrix ==[]:return maxCnt
        #
        # rows =len(matrix)
        # cols =len(matrix[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         cnt = 0
        #         if rows-i>=cnt and cols-j>=cnt:
        #
        #             tmpi=i
        #             tmpj=j
        #             while self.check(matrix,i,j,tmpi,tmpj):
        #                 cnt+=1
        #                 if(tmpi+1<rows and tmpj+1<cols):
        #                     tmpi+=1
        #                     tmpj+=1
        #                 else:
        #                     break
        #         maxCnt = max(maxCnt, cnt)
        # return maxCnt**2
        if matrix is None:return 0
        if len(matrix)==0 or len(matrix[0])==0:return 0
        rows =len(matrix)
        cols =len(matrix[0])
        dp=[[0]*cols]*rows
        maxCnt =0
        for i in range(0,rows):
            for j in range(0,cols):
                if i==0 or j==0:
                    dp[i][j] =int(matrix[i][j])
                elif matrix[i][j]=="1":
                    dp[i][j]=min(dp[i-1][j-1],min(dp[i][j-1],dp[i-1][j]))+1
                else:
                    dp[i][j]=0
                maxCnt =max(maxCnt,dp[i][j])
        return maxCnt**2
    def check(self,matrix,oi,oj,tmpi,tmpj):

        if matrix[tmpi][tmpj]=="1":
            for i in range(oi,tmpi)[::-1]:
                if matrix[i][tmpj]!="1":
                    return False
            for j in range(oj,tmpj)[::-1]:
                if matrix[tmpi][j]!="1":
                    return False
            return True
        else:
            return False

demo =Solution()
matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
param=demo.maximalSquare(matrix)
print(param)

