#To run the script: "python3 permutation.py"
#The script is written in Python 3

'''
  file   spanning_trees.py
  brief  Source code for finding all the spanning trees of a random, undirected graph
  author Dimitra Karatza
  AEM    8828
  date   2020-5-6
'''

from itertools import combinations
from collections import defaultdict
import numpy as np

# This class represents a undirected graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph


	# Function to add an edge to graph
	def addEdge(self,v,w):
		self.graph[v].append(w) #Add w to v_s list
		self.graph[w].append(v) #Add v to w_s list

	# A recursive function that uses visited[] and parent to detect
	# cycle in subgraph reachable from vertex v.
	def isCyclicUtil(self,v,visited,parent):

		#Mark the current node as visited
		visited[v]= True

		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			# If the node is not visited then recurse on it
			if visited[i]==False :
				if(self.isCyclicUtil(i,visited,v)):
					return True
			# If an adjacent vertex is visited and not parent of current vertex,
			# then there is a cycle
			elif parent!=i:
				return True

		return False


	#Returns true if the graph contains a cycle, else false.
	def isCyclic(self):
		# Mark all the vertices as not visited
		visited =[False]*(self.V)
		# Call the recursive helper function to detect cycle in different
		#DFS trees
		for i in range(self.V):
			if visited[i] ==False: #Don't recur for u if it is already visited
				if(self.isCyclicUtil(i,visited,-1))== True:
					return True

		return False

# This functions finds out if there is any circle in a graph
def containsCircle(graph,v):
	g1 = Graph(v)
	for i in range(v):
	    for j in range(v):
	        if (graph[i][j] == 1):
	            g1.addEdge(i,j)

	return g1.isCyclic()

# This function creates a random, undirected graph
def createGraph(v):
	# Create a random graph with 10 nodes
	graph  = np.random.randint(2,size=(v,v))

	# Keep only the upper diagonal array because we do not have directed graph
	for i in range(v):
	    for j in range(v):
	        if ((j <= i) & (graph[i][j] == 1)):
	            graph[j][i] = 1
	            graph[i][j] = 0

	return graph

# This function finds and prints all the spanning trees
def findSpanning(graph, v):
	# Convert the arry to a flat list without brackets
	flat_list = [item for sublist in graph for item in sublist]

	# Give to each element a value based on its position
	for i in range(len(flat_list)):
	    if flat_list[i] == 1:
	        flat_list[i] = i

	# Get rid of 0 elements
	new_list=[]
	for i in range(len(flat_list)):
	    if flat_list[i] != 0:
	        new_list.append(flat_list[i])

	# Take all the possible combinations of the elements
	edges = v-1
	combo = list(combinations(list(new_list), edges))

	# Create the array of the spanning tree from the combinations
	for i in combo:

	    # In new_list save the values of spanning tree
	    new_list=[]
	    for k in range(len(flat_list)):
	        if k in i:
	            new_list.append(1)
	        else:
	            new_list.append(0)

	    # Convert the flat new_list to an array
	    spanning = np.array(new_list).reshape(-1, v)

	    # Get rid of some new_list's which have circles
	    if(containsCircle(spanning,v) == False):
			# Spanning trees are printed inside the function
            # They are only stored temporarily in the value spanning
            # because of the extremelly big size of the problem
	        print(spanning,"\n")


# Main body of code
# Define number of vertices
v = 10
# Create a random graph
print("Created graph is:\n")
graph = createGraph(v)
print(graph,"\n")
# Find all the spanning trees of the created graph
print("Spanning trees are:\n")
findSpanning(graph, v)
