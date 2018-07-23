# Clayton Turner
# CS 317
# Project #2
# Python 3.5.2
import typing
import builtins
import statistics
import math

class TreeNode:

	def __iter__(self):
		"""the __iter__ function overrides the method for sprawling through the tree, such as for x in tree"""
		if self:
			if self.has_left():  # we have a left child node
				for kid in self.left:  # iterate over all the left nodes
					yield kid
			yield self
			if self.has_right():  # if the node has right kids
				for kid in self.right:
					yield kid

	def __init__(self, key : int, left: 'TreeNode' = None, right: 'TreeNode' = None, parent: 'TreeNode' = None):
		"""Function for creating nodes within the BST, initializes variables for
		key (int)
		parent node (Tree Node)
		left child (Tree Node)
		right child (Tree Node)"""

		self.key = key  # type: int
		self.parent = parent  # type: TreeNode
		self.right = right  # type: TreeNode
		self.left = left  # type: TreeNode

	def __str__(self):
		"""overrides the str() cast on the TreeNode object"""
		return str(self.key)

	def has_left(self):
		"""Does the node have a left leaf"""
		return self.left

	def has_right(self):
		"""Does the node have a right leaf?"""
		return self.right

	def isLeaf(self):
		"""returns true or false based on if it has any children"""
		return not (self.right or self.left)

	def has_both(self):
		"""returns true or false based on being a filled node"""
		return self.left and self.right


class BinarySearchTree:

	def __init__(self):
		"""constructor for creating the binary search tree object"""
		self.root = None  # type: TreeNode
		self.size = 0  # type: int
		self.comparisons = 0  # type: int

	def __iter__(self):
		"""the __iter__ function overrides the method for sprawling through the tree, such as for x in tree"""
		return self.root.__iter__()

	def __str__(self):
		"""overrides str() for this class returns a string-list of all the nodes"""
		nodelist = []
		for nodes in self:
			if nodes.key:
				nodelist.append(nodes.key)
		return str(nodelist)

	def insert(self, key: int):
		"""a public method for inserting an element into the tree"""
		self.size += 1
		if not self.root:
			self.root = TreeNode(key)
		else:
			self._insert(key, self.root)

	def _insert(self,key: int, current: TreeNode):
		"""Recursively look through the tree to find where a node should go. This is a private function."""
		if key < current.key:  # Is the key we're inserting less than the current one?
			if current.has_left():  # it is! does current have a left?
				self._insert(key, current.left)  # recursion
			else:  # since it does not have a left node, we're gonna give it a left node
				current.left = TreeNode(key, parent=current)
		else:  # it's greater than the current nodes key
			if current.has_right():  # does the node have a right child?
				self._insert(key, current.right)  # recursion
			else:  # the node doesn't have a right kid, so we're gonna place it.
				current.right = TreeNode(key, parent=current)

	def find(self, key: int):
		"""Loops over the tree, finds a node with the same key, returns that TreeNode object"""
		for node in self:
			if node.key == key:
				return node
			else:
				self.comparisons += 1
		raise KeyError("Value not in tree")

	def delete(self, key: int):
		"""deletes a node in the tree, by iterating over the tree
		if the key is not found, it adds it to the node list
		then it rebuilds the tree from scratch"""
		nodelist = []
		for node in self:
			if node.key != key:
				nodelist.append(node.key)
		self.root = None
		for item in nodelist:
			self.insert(item)

	def get_comparisons(self):
		temp = self.comparisons
		self.comparisons = 0
		return temp


class MagicList(list):
	"""class that subclasses list, used to override setitem and getitem to compare assignments (exchanges)"""
	def __init__(self, NumList : list):
		"""constructor for magic list class"""
		list.__init__(self, NumList)
		self.exchanges = 0

	def __getitem__(self, n : int):
		"""overrides the getitem dunder method, which is used to access elements in a object[key] fashion"""
		while len(self) <= n:
			self.append(self.dft)
		return super(MagicList, self).__getitem__(n)

	def __setitem__(self, key : int, value : int):
		"""overrides the setitem method to add +1 to exchanges, this replaces behavior for
		object[key] = value"""
		self.exchanges += 1
		return super(MagicList, self).__setitem__(key, value)


def heapify(arr : MagicList, n : int, i : int):
	"""recursive function for actually sorting. this gets called from heapSort()"""
	largest = i  # Initialize largest as root
	l = 2 * i + 1  # left = 2*i + 1
	r = 2 * i + 2  # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if less_than(l ,n) and less_than(arr[i], arr[l]):
		largest = l

	# See if right child of root exists and is
	# greater than root
	if less_than(r , n) and less_than(arr[largest] , arr[r]):
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # swap

		# Heapify the root.
		heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr : list):
	"""Driver function for heapsort. """
	n = len(arr)

	# Build a maxheap.
	for i in range(n, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]  # swap
		heapify(arr, i, 0)

def count(func : 'function'):
	"""decorator function reused from my first project
	basically used to store a counting variable."""
	def inner(*args):
		inner.counter += 1
		return func(*args)
	inner.counter = 0
	return inner

@count
def less_than(op1: int, op2: int):
	"""decorator annotated with @count means it calls count() whenever the function is called. returns x < y"""
	return op1 < op2

@count
def greater_than(op1: int, op2: int):
	"""decorator annotated with @count means it calls count() whenever the function is called. returns x > y"""
	return op1 > op2

if __name__ == "__main__":
	"""actual entry point for my code"""
	templist = []  # type: list holds list of all variables
	successfulComparisons = []  # type: list counter for successful comparisons
	unsuccessfulComparisons = []  # type: list counter for unsuccessful comparisons
	total = 0 #total number of comparisons made
	with open("alternating_order.txt") as f:
		"""read the file, append the items into templist, strip them and turn them into ints for easier processing"""
		for num in f:
			num = num.strip()
			templist.append(int(num))

	B = BinarySearchTree()  # type: BinarySearchTree
	for num in templist:
		"""create the binary tree and fill it in with values from the file"""
		B.insert(int(num))

	with open("search_values.txt") as f:
		"""open the file for searching. essentially, I read a value, strip the newline off the end, call the find method
		then I call get_comparisons() which will remove the value set in B.comparisons and hold it in a list to be 
		processed later. My Find function raises a KeyError when a value not in the tree is found, this makes it easy to
		distinguish if the value is being found or not, so the Exception block is run in the event of an unsuccessful 
		search"""
		for num in f:
			try:
				num = num.strip()
				B.find(int(num))
				temp = B.get_comparisons()
				successfulComparisons.append(temp)
			except KeyError:
				temp = B.get_comparisons()
				unsuccessfulComparisons.append(temp)

	"""print the values of total comparisons, called through the builtin sum() function which will iterate over an
	iterable, such as a list, and add all the values together.
	The statistics.mean() function is also built in and just returns the mean of the data."""
	print("Binary Search Tree:")
	print("Total Comparisons: {}".format(sum(unsuccessfulComparisons + successfulComparisons)))
	print("Average successful: {}".format(statistics.mean(successfulComparisons)))
	print("Average Unsuccessful: {}".format(statistics.mean(unsuccessfulComparisons)))



	"""building the HeapSort magic now"""
	heaplist = []  # type: list holds the list for heaping
	with open("random_order.txt") as f:
		"""build the list by iterating over the file"""
		for num in f:
			num = num.strip()
			heaplist.append(num)

		heaplist = MagicList(heaplist)  # type: MagicList convert the list to a MagicList for my exchange counter
		heapSort(heaplist)
		n = len(heaplist)
		print("\n*******************Heap Sort***************************")
		print("Number of comparisons for n * log2(n): {} and n^2: {}".format(n * math.log(n, 2), n**2))
		print("Comparisons for my implementation: {}".format(less_than.counter + greater_than.counter))
		print("Exchanges for my implementation: {}".format(heaplist.exchanges))


