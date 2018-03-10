# -*- coding: utf-8 -*-
# @Time    : 18-3-5 下午2:49
# @Author  : Yeh
# @Email   : mat_wu@163.com
# @File    : Sliding Window Maximum.py
# @Software: PyCharm

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or nums ==[]:return []
        first,last,i=0,k-1,k
        maxN=max(nums[0:k])
        res=[]
        res.append(maxN)
        last+=1
        while last<len(nums):
            if nums[first]<maxN:
                if nums[last]>maxN:
                    maxN = nums[last]
            else:
                    maxN=max(nums[first+1:last+1])
            res.append(maxN)
            first+=1
            last+=1
        return res




demo =Solution()
nums=[1,3,-1,-3,5,3,6,7]
print(demo.maxSlidingWindow(None,0))