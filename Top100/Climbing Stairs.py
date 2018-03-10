# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 11:22
# @Author  : Yeh
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre =cur=1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        return cur
demo = Solution()
print(demo.climbStairs(4))