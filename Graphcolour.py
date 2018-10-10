class Graph():

    def __init__(self, vert):
        self.V = vert
        self.graph = [[0 for column in range(vert)] \
                      for row in range(vert)]


    def Safe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def gColor(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.Safe(v, colour, c) == True:
                colour[v] = c
                if self.gColor(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.gColor(m, colour, 0) == False:
            return False

        print "Solution exist, Colours:"
        for c in colour:
            print c,
        return True


print "Enter no of Vertices : "
ver=input()
g = Graph(ver)

print "Enter Adjacency Matrix"
mat=[[0 for j in range(ver)] for i in range(ver)]

print mat
for i in range (0,ver):
  for j in range (0,ver):
    print "Entry in row: ",i+1," column: ",j+1
    mat[i][j] = input()


g.graph = mat
print "Enter No of colours - "
m = input()
g.graphColouring(m)