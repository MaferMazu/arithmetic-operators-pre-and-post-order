class Node:
    """ Represent a node in binary tree """
    def __init__(self, string,left=None,right=None):
        self.left = left
        self.right = right
        self.string = string

    def __str__(self):
        return "("+str(self.left)+str(self.string)+str(self.right)+")"
