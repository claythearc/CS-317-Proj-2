# Clayton Turner
# CS 317
# Project #2
# Python 3.5.2

import typing
import builtins



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

    def delete2(self, key: int):
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


if __name__ == "__main__":
    B = BinarySearchTree()
    import random
    rlist = []
    for i in range(0, 100):
        x = random.randint(1, 400)
        rlist.append(x)
        B.insert(x)
    print(rlist)
    print(B)
    B.delete2(rlist[0])
    print(B)