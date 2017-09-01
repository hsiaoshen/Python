#coding=utf-8

# 实现矩阵按照从外向里按照顺时针的方式打印出来
def printMatrix(matrix):
    res=[]
    n=len(matrix)
    m=len(matrix[0])
    if m==1 and n==1:
        res=[matrix[0][0]]
        return res
    else:
        for o in range((min(m,n)+1)//2):
            [res.append(matrix[o][i]) for i in range(o,m-o)]
            [res.append(matrix[j][m-o-1]) for j in range(o,n-o) if matrix[j][m-o-1] not in res]
            [res.append(matrix[n-o-1][k]) for k in range(m-1-o,o-1,-1) if matrix[n-o-1][k] not in res]
            [res.append(matrix[l][o]) for l in range(n-1-o,o-1,-1) if matrix[l][o] not in res]
        return res


if __name__ == "__main__":
    lists = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16,]
    ]

    l0 = printMatrix(lists)
    print l0
