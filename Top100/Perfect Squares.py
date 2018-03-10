# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 22:45
# @Author  : Yeh
import sys
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp =[0]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            j=1
            minNum = sys.maxsize
            while i-j*j>=0:
                minNum =min(minNum,dp[i-j*j]+1)
                j+=1
            dp[i]=minNum
        return dp[n]

demo =Solution()
param=demo.numSquares(12)
print(param)
