import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from main import *


class TestMain(unittest.TestCase):

    def test_convert_expr_pre_base(self):
        result=convert_expr("PRE",["+","3","4"])
        self.assertEqual(result,"(3+4)")

    def test_covert_expr_pre_heavy(self):
        result=convert_expr("PRE",["+","*","1","-","6","/","6","2","+","+","1","1","1"])
        self.assertEqual(result,"((1*(6-(6/2)))+((1+1)+1))")

    def test_convert_expr_post_base(self):
        result=convert_expr("POST",["3","4","+"])
        self.assertEqual(result,"(3+4)")

    def test_convert_expr_post_heavy(self):
        result=convert_expr("POST",["1","6","6","2","/","-","*","1","1","+","1","+","+"])
        self.assertEqual(result,"((1*(6-(6/2)))+((1+1)+1))")

    def test_convert_expr_none(self):
        result=convert_expr("POSTER",["1","6","6","2","/","-","*","1","1","+","1","+","+"])
        self.assertEqual(result,None)



if __name__ == "__main__":
    unittest.main()