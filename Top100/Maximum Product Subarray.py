# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 10:40
# @Author  : Yeh


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None:
            return 0
        f =[0]*len(nums)
        g =[0]*len(nums)
        f[0]=nums[0]
        g[0]=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            f[i]=max(max(f[i-1]*nums[i],g[i-1]*nums[i]),nums[i])
            g[i]=min(min(f[i-1]*nums[i],g[i-1]*nums[i]),nums[i])
            res =max(res,f[i])
        return res
demo =Solution()
nums =[-2,3,-2]
print(demo.maxProduct(nums))