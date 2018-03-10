
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left=[0]*n
        right=[0]*n
        for i in range(1,n):
            left[i]=max(height[i-1],left[i-1])
            right[n-i-1]=max(height[n-i],right[n-i])
        sum=0
        for i in range(1,n):
            if min(left[i],right[i])>height[i]:
                sum+=min(left[i],right[i])-height[i]
        return sum


s = Solution()
nums=[0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(nums))