from sys import exit
from formater import *

def main():
    print("*"*30)
    print("""Welcome to this simulator of arithmetic operations
    in pre and post order :D Happy coding\n""")
    while True:
        my_input=input(">> ")
        my_input=my_input.upper()
        elems=my_input.split(" ")
        command=elems[0]
        if command=="LEAVE":
            exit(0)
        elif command=="EVAL" and len(elems)>1:
            order=elems[1]
            if order=="PRE"or order=="POST" and len(elems)>2:
                expr=elems[2:]
                try:
                    my_expr=convert_expr(order,expr)
                    try:
                        print(eval(my_expr))
                    except:
                        print("Arithmetic Error")
                        print("You try to evaluate "+my_expr)
                except:
                    print("Expression Error")
                    print("Please enter a correct orden of elements")
                    print("Remember you are using "+str(order))
            else:
                print_help("order")

        elif command=="SHOW" and len(elems)>1:
            order=elems[1]
            if order=="PRE"or order=="POST" and len(elems)>2:
                expr=elems[2:]
                my_expr=convert_expr(order,expr)
                print(my_expr)
            else:
                print_help("order")
        else:
            print_help()

def convert_expr(order,expr):
    if order=="PRE":
        return string_from_preorder(expr)
    elif order=="POST":
        return string_from_postorder(expr)
    else:
        return None

def print_help(option=None):
    """ Print help for user """

    response="""Try with valid format:
    EVAL <order> <expr>
    SHOW <order> <expr>
    LEAVE
    
    <order> must be: PRE or POST
    <expr> is something like:
    + * + 3 4 5 7
    8 3 - 8 4 4 + * +
    and depends if you use pre or post order.
    
    If you need more information read the README file\n"""

    if option=="order":
        response=response[:24]+response[87:]

    elif option=="expr":
        response=response[:24]+response[118:]

    print(response)


if __name__ == "__main__":
    main()