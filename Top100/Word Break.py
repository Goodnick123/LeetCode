# -*- coding: utf-8 -*-
# @Time    : 2018/2/23 9:59
# @Author  : Yeh


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if  s==None or len(s)==0:
            return True
        if wordDict==[] or wordDict==None:
            return False
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if dp[i]==True:
                    if s[i:j+1] in dict:
                        dp[j+1]=True
        return dp[len(s)]


demo =Solution()
s = "leetcode"
dict = ["leet", "codee"]
print(demo.wordBreak(s,dict))