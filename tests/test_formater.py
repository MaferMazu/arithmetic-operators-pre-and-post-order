import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from formater import *

class TestOfPreOrder(unittest.TestCase):
    def test_one_number(self):
        result=string_from_preorder(["3"])
        self.assertEqual(result,"3")
    
    def test_one_operator_plus(self):
        result=string_from_preorder(["+","3","4"])
        self.assertEqual(result,"(3+4)")

    def test_one_operator_div(self):
        result=string_from_preorder(["/","3","4"])
        self.assertEqual(result,"(3/4)")

    def test_exam_example1(self):
        result=string_from_preorder(["+","*","+","3","4","5","7"])
        self.assertEqual(result,"(((3+4)*5)+7)")

    def test_exam_example2(self):
        result=string_from_preorder(["+","-","8","3","*","8","+","4","4"])
        self.assertEqual(result,"((8-3)+(8*(4+4)))")

    def test_tree_binary_complete_two_levels(self):
        result=string_from_preorder(["+","-","1","2","*","3","4"])
        self.assertEqual(result,"((1-2)+(3*4))")

    def test_tree_with_one_number_right(self):
        result=string_from_preorder(["+","1","+","+","1","1","1"])
        self.assertEqual(result,"(1+((1+1)+1))")
    
    def test_tree_with_one_number_left(self):
        result=string_from_preorder(["+","+","+","1","1","1","1"])
        self.assertEqual(result,"(((1+1)+1)+1)")

    def test_tree_with_two_nodes_in_third_level(self):
        result=string_from_preorder(["+","*","-","3","4","-","2","1","7"])
        self.assertEqual(result,"(((3-4)*(2-1))+7)")

    def test_tree_with_varius_levels(self):
        result=string_from_preorder(["+","*","1","-","6","/","6","2","+","+","1","1","1"])
        self.assertEqual(result,"((1*(6-(6/2)))+((1+1)+1))")

class TestOfPostOrder(unittest.TestCase):
    def test_one_number(self):
        result=string_from_postorder(["3"])
        self.assertEqual(result,"3")
    
    def test_one_operator_plus(self):
        result=string_from_postorder(["3","4","+"])
        self.assertEqual(result,"(3+4)")

    def test_one_operator_div(self):
        result=string_from_postorder(["3","4","/"])
        self.assertEqual(result,"(3/4)")

    def test_exam_example1(self):
        result=string_from_postorder(["5","4","4","+","*"])
        self.assertEqual(result,"(5*(4+4))")

    def test_exam_example2(self):
        result=string_from_postorder(["8","3","-","8","4","4","+","*","+"])
        self.assertEqual(result,"((8-3)+(8*(4+4)))")

    def test_tree_binary_complete_two_levels(self):
        result=string_from_postorder(["1","2","-","3","4","*","+"])
        self.assertEqual(result,"((1-2)+(3*4))")

    def test_tree_with_one_number_right(self):
        result=string_from_postorder(["1","1","1","+","1","+","+"])
        self.assertEqual(result,"(1+((1+1)+1))")
    
    def test_tree_with_one_number_left(self):
        result=string_from_postorder(["1","1","+","1","+","1","+"])
        self.assertEqual(result,"(((1+1)+1)+1)")

    def test_tree_with_two_nodes_in_third_level(self):
        result=string_from_postorder(["3","4","+","2","1","-","*","7","+"])
        self.assertEqual(result,"(((3+4)*(2-1))+7)")

    def test_tree_with_varius_levels(self):
        result=string_from_postorder(["1","6","6","2","/","-","*","1","1","+","1","+","+"])
        self.assertEqual(result,"((1*(6-(6/2)))+((1+1)+1))")


if __name__ == "__main__":
    unittest.main()