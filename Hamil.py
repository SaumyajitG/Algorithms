class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)] \
                      for row in range(vertices)]
        self.V = vertices


    def Safe(self, v, pos, path):

        if self.graph[path[pos - 1]][v] == 0:
            return False


        for vertex in path:
            if vertex == v:
                return False

        return True


    def hamUtil(self, path, pos):


        if pos == self.V:

            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False


        for v in range(1, self.V):

            if self.Safe(v, pos, path) == True:
                path[pos] = v

                if self.hamUtil(path, pos + 1) == True:
                    return True


                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V


        path[0] = 0

        if self.hamUtil(path, 1) == False:
            print "Solution does not exist\n"
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print "Solution Exists: Following is a Hamiltonian Cycle"
        for vertex in path:
            print vertex,
        print path[0], "\n"



print "Enter no of Vertices : "
ver=input()


graph1 = Graph(ver)

print "Enter Adjacency Matrix"
mat=[[0 for j in range(ver)] for i in range(ver)]

print mat
for i in range (0,ver):
  for j in range (0,ver):
    print "Entry in row: ",i+1," column: ",j+1
    mat[i][j] = input()

graph1.graph = mat

graph1.hamCycle();