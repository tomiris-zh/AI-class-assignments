#Assignment 3
from as3_tree import Tree
class Result:
	def __init__(self, sol=[], val=-1000):
			self.solution = sol
			self.value = val
			
class MNX:
	def __init__(self, data_list):
		self.tree = Tree()	
		self.tree.init_tree(data_list)
		self.root = self.tree.root
		self.currentNode = None
		self.successors = []
		self.traversed = [] # elements in the list are in the form of [node, optimal_child]		
		return

	# Starts from a root and searches most optimal child, then its most optimal child and so on:
	def result_from_traversed(self):
		res = []
		cur = self.traversed[-1] # last: [root, ...]
		res.append(cur[0])
		while cur[1] is not None: # leaf: [..., None]
			for elements in self.traversed:
				if elements[0] == cur[1]:
					cur = elements
					break
			res.append(cur[0])
		return res

	def terminalTest(self, node):
		assert node is not None
		return len(node.children) == 0

	def utilityChecking(self, node):
		assert node is not None
		return node.value

	def getChildren(self, node):
		assert node is not None
		return node.children

	def minimax(self):		
		terminal_val = self.max_v(self.root)
		successors = self.getChildren(self.root)
		res=Result()


#################  Return the solution here  #################
		res.value=terminal_val #you put the best terminal value for root node here
		res.solution=list(map(lambda node: node.Name, self.result_from_traversed())) #you put the solution_array here
#################  Return the solution here  #################



		return res


	def max_v(self, node):		
		if self.terminalTest(node):
			self.traversed.append([node, None]) # appending leafs
			return self.utilityChecking(node)		
		max_v = -1000 #we use -1000 as the initial_maximum value
		max_node = None
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			variant = self.min_v(deeper_node)
			if max_v < variant:
				max_v = variant
				max_node = deeper_node
		self.traversed.append([node, max_node]) # appending [parent, optimal_child] pair
		return max_v

	def min_v(self, node):		
		if self.terminalTest(node):
			self.traversed.append([node, None]) # appending leafs
			return self.utilityChecking(node)
		min_v = 1000 #we use 1000 as the initial_minimum value
		min_node = None
		deeper_layer = self.getChildren(node)
		for deeper_node in deeper_layer:
			variant = self.max_v(deeper_node)
			if min_v > variant:
				min_v = variant
				min_node = deeper_node
		self.traversed.append([node, min_node]) # appending [parent, optimal_child] pair
		return min_v