# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 15:33
# @Author  : Yeh

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums ==[]:return 0
        if len(nums)<3:
            return max(nums)
        dp =[0]*len(nums)
        dp[0] =nums[0]
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            if i-3 >=0 and i-2>=0:
                dp[i] =max(max(nums[i]+dp[i-3],nums[i]+dp[i-2]),dp[i-1])
            else:
                dp[i] =max(nums[i]+dp[i-2],dp[i-1])
        return dp[len(nums)-1]


demo =Solution()
nums= [1,3,1]
print(demo.rob(nums))
