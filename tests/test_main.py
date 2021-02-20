import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from main import *


class TestMain(unittest.TestCase):

    """ @unittest.mock.patch('builtins.print')
    @unittest.mock.patch('main.input')
    def test_read_all_class(self,mocked_input,mocked_print):
        mocked_input.side_effect = "EVAL PRE + * + 3 4 5 7"
        main(1)
        mocked_print.assert_called_with("")
        
        #print(result)
        self.assertTrue(True) """

    """ def test_only_numbers(self):
        self.assert_stdout(main(), '') """

    """ @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_print_help(self):
        print_help()
        captured = self.capsys.readouterr()
        self.assertEqual('eggs\n', captured.out) """

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