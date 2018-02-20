import sys #access to command line arguments


class DirectedGraph:
    def __init__(self, graph = None):

        if graph == None:
            print("**Creating Graph**")
            graph = {}

        self.graph = graph

    #adds an edge between two vertex, using the structure dictionary inside a dictionary first key being the source and inner key being
    #the destination the value of the innerkey is the weight
    def AddEdge(self, source, destination, weight):
        print("**In ADDEDGE**")
        if source not in self.graph:
            print("Not In Graph: ", source)
            #add vertex to graph
            self.graph[source] = {}
            self.graph[source][destination] = weight

        else:
            print("In graph: ", source)
            #add only the edge and weight to dict key
            self.graph[source][destination] = weight



    def PrintGraph(self):
        print(self.graph)


    #implemented using a queque(FIFO), and we keep track to the vertexes visited using a boolean array
    def SearchBFS(self):
        print("INSIDE BFS")
        visited = [False]*(len(self.graph)) #boolean array
        print(visited)

        que = []

        #add the starting vertex

        print(que)


def main():

    print("num of arg:", len(sys.argv))
    print("Argument list", str(sys.argv))

    #check that all arguments were passed
    # try:
    #     fileName = str(sys.argv[1])
    #     # startNode = str(sys.argv[2])
    #     # endNode = str(sys.argv[3])
    #     # searchType = str(sys.argv[4])
    # except:
    #     print("ERROR one/all Command line arguments not entered")
    #     sys.exit(1)

    # print(fileName,startNode, endNode,searchType )

    file = open("input_file")
    fileLines = file.readlines()

    graph = DirectedGraph()
    #seperate files input, first number is that edge's source, and the second number is that edge's destination. The third number on a line represents the weight of that edge
    for line in fileLines:
        source, destination, weight = line.split()

        print("edge Source", source)
        print("edge destination", destination)
        print("weight", weight)
        print()
        graph.AddEdge(source,destination,weight)


    graph.PrintGraph()
    graph.SearchBFS()



main()