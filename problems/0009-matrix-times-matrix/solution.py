def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    c=[]
    if len(a[0])!=len(b):
         return -1
    for i in range(len(a)):
        res=[]
        for j in range(len(b[0])):
            s=0
            for k in range((len(a[0]))):
                s+=a[i][k]*b[k][j]
            res.append(s)
        c.append(res)
    return c