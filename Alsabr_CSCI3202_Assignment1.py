# Yousef Alsabr
# 102056080
# CSCI3202 Assignment 1


import Queue
import random

class Queue:
	# initialize queeue
    
    q = Queue.Queue()
    def __init__(self):
        pass
	
	# First check if the added value is an int
	# Then Add the value
    def push_queue(self, value): 
        if isinstance(value, int):
            self.q.put(value)
            return True
        else:
            print("Queue supports only integers")
            return False
	# Dequeue
    def pop_queue(self):
        return self.q.get()
	s
	# Check if Empty
    def isEmpty(self):
        return self.q.empty()
	
	# Get size
	def get_size(self):
		return self.q.size()

class Stack(object):
    
    # initialize
    def __init__(self):
		self.st = []
		self.size = 0
	
	
    def checkSize(self):
		return len(self.st)
        
    def isEmpty(self):
		return (self.checkSize() == 0)
        
	# Add to stack only if int
    def push(self, myInt):
		if isinstance(myInt, int):
			self.st.append(myInt)
			return True
		else:
			print("Stack supports only integers.")
			return False

    def pop(self):
        if self.isEmpty():
            print("Can't pop from empty stack")
        else:
			return self.st.pop()
     
class Node():

    def __init__(self, key, parent):
        #create node only specifying the key value
        #assignment of parent and children will be handled by methods
        if not isinstance(key, int):
            print("Nodes only support int")
            return
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
   
    def __str__(self):
		# Recursively collect all values in a string
		base = str(self.key)
		if self.left != None:
			base += ", "
			base += str(self.left)
		if self.right != None:
			base += ", "
			base += str(self.right)
		return base


class Tree:
    def __init__(self, key):
        self.root = Node(key, None)

    def add(self, value, parentNode):
		
		# Search form the root node
        nodes = [self.root]
        while len(nodes):
            current_node = nodes[0]

            # Check every Tree node for the parent value
            if current_node.key == parentNode:
                if current_node.left == None:
                    current_node.left = Node(value, current_node)
                    return True
                elif current_node.right == None:
                    current_node.right = Node(value, current_node)
                    return True
                else:
                    print("Parent has two children, node not added")
                    return False

            # Push this node's children, pop this node
            # And don't increment index (0)
            if current_node.left != None:
                nodes.append(current_node.left)
            if current_node.right != None:
                nodes.append(current_node.right)
            nodes.pop(0)

        print("Parent not found")
        return False

    def delete(self, value):
        
        # Seach form the root node
        nodes = [self.root]
        while len(nodes):
            current_node = nodes[0]

            if current_node.key == value:
                if current_node.left == None and current_node.right == None:
                    if current_node.parent.left == current_node:
                        current_node.parent.left = None
                        del current_node
                        return True
                    elif current_node.parent.right == current_node:
                        current_node.parent.right = None
                        del current_node
                        return True
                    else:
                        del current_node
                        return False   
                else:
                    print("Node not deleted, has children")
                    return False

            # Push this node's children, pop this node
            # And don't increment index (0)
            if current_node.left != None:
                nodes.append(current_node.left)
            if current_node.right != None:
                nodes.append(current_node.right)
            nodes.pop(0)

        print("Node not found")
        return False

    def printTree(self):
        print("[" + str(self.root) + "]")



class Graph:
    def __init__(self):
		self.dict = {}

    def addVertex(self, value):
        if value in self.dict:
            print("Vertex already exists")
        else:
            # Create a new key from value, and have it map to
            # a blank list, to store adjacent edges
            self.dict[value] = []

    def addEdge(self, value1, value2):
        if (value1 not in self.dict) or (value2 not in self.dict):
            print("One or more vertices not found.")
        else:
            if value2 in self.dict[value1] or value1 in self.dict[value2]:
                print("Edge already in Graph")
                return False
            else:
                # Add each node to the other's list of adjacent edges
                self.dict[value1].append(value2)
                self.dict[value2].append(value1)
                return True

    def findVertex(self, value):
        if value in self.dict:
            print(self.dict[value])
        else:
            print("Vertex not found")

def main():
	
	print("Yosuef Alsabr")
	print("CSCI Assignment 1")
	print("Testing code")
	
	print("//////////// Testing: Queue //////////////////")
	print("")
	
	myQueue = Queue()
	
	print("Adding 10 random values to MyQueue:")
	
	for _ in range(10):
		randInt = random.randrange(100)
		print "Adding", randInt
		myQueue.push_queue(randInt)
	
	print("")
	print("Dequeueing values now:")
	
	for _ in range(10):
		print "Dequeueing", myQueue.pop_queue()
	
	
	print("")
	print("//////////// Testing: Stack //////////////////")
	print("")
	
	
	myStack = Stack()
	
	
	print("Adding 10 random values to Stack")
	for _ in range(10):
		randInt = random.randrange(100)
		myStack.push(randInt)
		print "Adding", randInt
	
	print "Checking size:", myStack.checkSize()
	
	print("")	
	print("Pop the 10 randomg values from the stack.")
	
	for _ in range(10):
		print "Popped", myStack.pop()
	
	print  "Checking size:", myStack.checkSize()
	
	
	print("")
	print("//////////// Testing: Tree //////////////////")
	print("")
	
	myTree = Tree(0)
	print("Adding 10 valuse to tree:")
	myTree.add(1, 0)
	myTree.add(2, 0)
	myTree.add(3, 1)
	myTree.add(4, 1)
	myTree.add(5, 2)
	myTree.add(6, 2)
	myTree.add(7, 3)
	myTree.add(8, 3)
	myTree.add(9, 4)
	myTree.printTree()
	
	print("")
	print("Deleting values:")
	print("Deleteing the 7:")
	myTree.delete(7)
	print("Deleteing the 5:")
	myTree.delete(5)
	print("")
	myTree.printTree()
	
	print("")
	print("Trying to delete un-deletable values:")
	myTree.delete(0)
	myTree.delete(1)
	
	print("")
	print("Trying to delete non-existing value:")
	myTree.delete(99)
	print("")
	print("Tree now:")
	myTree.printTree()
	print("")
	
	
	print("")
	print("//////////// Testing: Graph //////////////////")
	print("")
	
	
	myGraph = Graph()
	
	print("Adding 10 random valuse as vertices to the graph:")
	
	for i in range(10):
		myGraph.addVertex(i)
	myGraph.addVertex(10)
	
	print("")
	print("Adding already existing Vertex: ")
	myGraph.addVertex(1)
	
	print("")
	print("Adding 20 edges to the graph:")
	edges = [(0,1), (2,3), (4,5), (6,7), (8,9),
                  (0,2), (0,3), (0,4), (0,5), (0,6),
                  (0,7), (0,8), (0,9), (2,4), (2,6),
                  (2,8), (4,6), (4,8), (6,8), (3,7)]
	
	for i in edges:
		myGraph.addEdge(i[0],i[1])
	
	print("")
	print("Vertex 0 edges should be [1,2,3,4,5,6,7,8,9]:")
	myGraph.findVertex(0)
	print("")
	print("Vertex 1 edges should be [0]:")
	myGraph.findVertex(1)
	print("")
	print("Vertex 3 edges should be [0,2,7]:")
	myGraph.findVertex(3)
	print("")
	print("Vertex 6 edges should be [0,2,4,7,8]:")
	myGraph.findVertex(6)
	print("")
	print("Vertex 9 edges should be [0,8]:")
	myGraph.findVertex(9)
	print("")
	
	print("//////////// Testing: Ends //////////////////")
	
	
	

if __name__ == '__main__':
	main()

