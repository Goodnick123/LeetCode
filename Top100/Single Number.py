# -*- coding: utf-8 -*-
# @Time    : 2018/2/22 20:25
# @Author  : Yeh

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m =dict(zip(nums,[2]*len(nums)))
        for i in nums:
            m[i]=m.get(i)-1
            if m[i]==0:
                m.pop(i)
        res=None
        for a,b in m.items():
            res=a
        return res
nums=[]
demo =Solution()
print(demo.singleNumber(nums))
