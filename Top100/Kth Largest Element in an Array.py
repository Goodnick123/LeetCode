# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 13:08
# @Author  : Yeh

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None:return 0
        tmp =sorted(nums[0:k])
        for i in range(k,len(nums)):
            if nums[i]>=tmp[-1]:
                del tmp[0]
                tmp.append(nums[i])
            elif nums[i]>tmp[0] and nums[i]<tmp[-1]:
                del tmp[0]
                tmp.append(nums[i])
                tmp=sorted(tmp)
        return tmp[0]



demo =Solution()
nums=[3,2,3,1,2,4,5,5,6]
param =demo.findKthLargest(nums,4)
print(param)
