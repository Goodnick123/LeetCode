class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic ={}
        res=[]
        index=0;
        for i in range(len(strs)):
            str ="".join(sorted(strs[i]))
            if dic.get(str) is not None:
                res[dic.get(str)].append(strs[i])
            else:
                dic[str] = index
                res.append([strs[i]])
                index+=1
        return res

s = Solution()
strs= ["eat","tea","tan","ate","nat","bat"]
s.groupAnagrams(strs)

