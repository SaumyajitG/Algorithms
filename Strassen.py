def Matinit(p, q):
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix


def split(matrix): 
    a = matrix
    b = matrix
    c = matrix
    d = matrix
    while(len(a) > len(matrix)/2):
        a = a[:len(a)/2]
        b = b[:len(b)/2]
        c = c[len(c)/2:]
        d = d[len(d)/2:]
    while(len(a[0]) > len(matrix[0])/2):
        for i in range(len(a[0])/2):
            a[i] = a[i][:len(a[i])/2]
            b[i] = b[i][len(b[i])/2:]
            c[i] = c[i][:len(c[i])/2]
            d[i] = d[i][len(d[i])/2:]
    return a,b,c,d

def MatAdd(a, b):
    if type(a) == int:
        d = a + b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] + b[i][j])
            d.append(c)
    return d

def MatSub(a, b):
    if type(a) == int:
        d = a - b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] - b[i][j])
            d.append(c)
    return d


def strassen(a, b, q):
    # base case: 1x1 matrix
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)

        p1 = strassen(MatAdd(a11,a22), MatAdd(b11,b22), q/2)

        p2 = strassen(MatAdd(a21,a22), b11, q/2)

        p3 = strassen(a11, MatSub(b12,b22), q/2)

        p4 = strassen(a22, MatSub(b21,b11), q/2)

        p5 = strassen(MatAdd(a11,a12), b22, q/2)

        p6 = strassen(MatSub(a21,a11), MatAdd(b11,b12), q/2)

        p7 = strassen(MatSub(a12,a22), MatAdd(b21,b22), q/2)


        c11 = MatAdd(MatSub(MatAdd(p1, p4), p5), p7)

        c12 = MatAdd(p3, p5)
        
        c21 = MatAdd(p2, p4)

        c22 = MatAdd(MatSub(MatAdd(p1, p3), p2), p6)

        c = Matinit(len(c11)*2,len(c11)*2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]= c11[i][j]
                c[i][j+len(c11)]= c12[i][j]
                c[i+len(c11)][j]= c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c

print "Enter dimensions mxn of matrix 1:"
m=input()
arr=Matinit(m,m)
arr1=Matinit(m,m)
print "Enter values of matrix 1 - "
for i in range(m):
    for j in range(m):
        arr[i][j]=input()

print "Enter values of matrix 2 - "
for i in range(m):
    for j in range(m):
        arr1[i][j]=input()

print "Matrix mult:"
print strassen(arr, arr1, m)