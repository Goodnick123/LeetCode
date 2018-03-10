class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates =sorted(candidates)
        res =[]
        list=[]
        self.dfs(candidates,target,0,list,res)
        return res
    def dfs(self,candidates,target,index,list,res):
        if target<0:
            return
        elif target ==0:
            res.append(list.copy())
        else:
            for i in range(index,len(candidates)):
                list.append(candidates[i])
                self.dfs(candidates,target-candidates[i],i,list,res)
                del list[len(list)-1]

s =Solution()
nums=[]
res =s.combinationSum(nums,7)
print(res)