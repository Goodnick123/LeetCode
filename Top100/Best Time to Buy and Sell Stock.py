# -*- coding: utf-8 -*-
# @Time    : 2018/2/21 12:08
# @Author  : Yeh

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:return 0
        dp=[0]*len(prices)
        maxNum=0
        dp[0]=prices[0]
        for i in range(1,len(prices)):
            dp[i]=min(prices[i],dp[i-1])
            maxNum = max(prices[i]-dp[i],maxNum)
        return maxNum


demo =Solution()
arr =[]
demo.maxProfit(arr)


