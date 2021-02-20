import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from node import Node

class TestOfNode(unittest.TestCase):
    def test_create_node(self):
        node1=Node("+","1","2")
        self.assertTrue(isinstance(node1,Node))
    
    def test_print_simple_node(self):
        node1=Node("+","1","2")
        self.assertEqual("(1+2)",str(node1))

    def test_print_node_with_one_node(self):
        node1=Node("+","1","2")
        node2=Node("-","5",node1)
        self.assertEqual("(5-(1+2))",str(node2))

    def test_print_node_with_multiples_nodes(self):
        node1=Node("+","1","2")
        node2=Node("-","5",node1)
        node3=Node("+","1","2")
        node4=Node("*",node2,node3)
        self.assertEqual("((5-(1+2))*(1+2))",str(node4))


if __name__ == "__main__":
    unittest.main()