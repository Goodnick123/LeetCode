# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res=[]
        intervals.sort(key=lambda x:x.start)
        for i in range(0,len(intervals)):
            if i==0:
                res.append(intervals[i])
            else:
                tmp =res[len(res)-1]
                if intervals[i].start>tmp.end:
                    res.append(intervals[i])
                else:
                    tmp.end = max(intervals[i].end,tmp.end)
        return res


demo = Solution()
in1 =Interval(1,3)
in2 =Interval(2,6)
in3=Interval(8,10)
in4=Interval(15,18)
arr=[]
# arr.append(in2)
# arr.append(in1)
# arr.append(in3)
# arr.append(in4)
res= demo.merge(arr)
for i in range(len(res)):
    print(res[i].start,res[i].end)
