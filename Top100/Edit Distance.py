# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 9:50
# @Author  : Yeh

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        rows =len(word1)+1
        cols = len(word2)+1
        dp=[0]*rows
        for i in range(rows):
            dp[i]=[0]*cols
        dp[0]=[i for i in range(cols)]
        for i in range(rows):
            dp[i][0] =i
        for i in range(1,rows):
            for j in range(1,cols):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] =dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
        return dp[rows-1][cols-1]
demo =Solution()
print(demo.minDistance("a","b"))