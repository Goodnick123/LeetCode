class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum=nums[0]
        sum=nums[0]
        for i in range(1,len(nums)):
            if sum<0:
                sum=0
            sum+=nums[i]
            maxNum=max(sum,maxNum)
        return maxNum

s= Solution()
arr=[1,2]
print(s.maxSubArray(arr))