#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2
def traverse(tree, init):    	
	queue = [init]
	traversed = []
	while queue:
		'''
			Student fixes the loopy path from here to the end of this function
		'''
		node = queue.pop(0)
		if node not in traversed:
			traversed.append(node)
			leaves = tree[node]
			for leaf in leaves:
				queue.append(leaf)
	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"
	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node == goal:
			return path
		elif node not in traversed:
			for adjacent in tree.get(node, []):
				new_path = list(path)
				new_path.append(adjacent)
				queue.append(new_path)
			traversed.append(node)
		'''
			You implement the path finder from here
		'''
	#	break
	return "No such path exists"
 
