class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(0,rows):
            for j in range(0,cols-i):
                self.swap(matrix,i,j,rows-j-1,cols-i-1)
        for i in range(0,int(rows/2)):
            for j in range(0,cols):
                self.swap(matrix,i,j,cols-i-1,j)
        print(matrix)


    def swap(self,matrix,i,j,m,n):
        tmp =matrix[i][j]
        matrix[i][j]=matrix[m][n]
        matrix[m][n] = tmp

    def deep(self,matrix):
        matrix[::]=zip(*matrix[::-1])
        print(matrix)

s=Solution()
matrix=[
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
s.deep(matrix)
#s.rotate(matrix)
