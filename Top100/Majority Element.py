# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 22:20
# @Author  : Yeh
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res={}
        for i in nums:
            res[i] =res.get(i,0)+1
        return max(res.items(), key=lambda x: x[1])[0]

        # return sorted(nums)[len(nums) // 2]

demo =Solution()
nums=[1,1,2,1,2,3]
print(demo.majorityElement(nums))
