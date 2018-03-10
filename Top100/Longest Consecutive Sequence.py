# -*- coding: utf-8 -*-
# @Time    : 2018/2/22 11:33
# @Author  : Yeh


class Solution:
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     lst =set(nums)
    #     res=0
    #     for i in nums:
    #         if i in lst:
    #             lst.remove(i)
    #             pre=i-1;next =i+1
    #             while pre in nums :
    #                 lst.remove(pre)
    #                 pre-=1
    #             while next in nums :
    #                 lst.remove(next)
    #                 next+=1
    #             res =max(res,next-pre-1)
    #
    #             res=max(res,next-pre-1)
    #     return res

    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


demo =Solution()
arr=[100, 4, 200, 1, 3, 2]
print(demo.longestConsecutive(arr))
