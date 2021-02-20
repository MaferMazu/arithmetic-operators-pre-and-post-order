from node import Node
OPERATORS=["*","/","+","-"]

def string_from_preorder(mylist):
    """ Function that convert list in preorder to the arithmetic expression
    Input:
        mylist : list
            Elements to analize and convert
    Output:
        return : str
            Arithmetic expression in string"""

    if not mylist[0] in OPERATORS and len(mylist)==1:
        return str(mylist[0])
    elif len(mylist)==3:
        return str(Node(mylist[0],mylist[1],mylist[2]))
    else:
        for i in range(1,len(mylist)-2):
            if mylist[i] in OPERATORS:
                
                with_simbol=False
                for j in range(i,len(mylist)+1):
                    if mylist[j] in OPERATORS:
                        with_simbol=True
                        break

                if i+3<len(mylist) and not mylist[i+3] in OPERATORS and not (i-2>0 and not mylist[i-2] in OPERATORS) and not with_simbol:
                    pass
                else:
                    if not mylist[i+1] in OPERATORS and not mylist[i+2] in OPERATORS:
                        temp=mylist[i]
                        mylist[i]=str(Node(temp,mylist[i+1],mylist[i+2]))
                        del mylist[i+1]
                        del mylist[i+1]
                        break
        return string_from_preorder(mylist)


def string_from_postorder(mylist):
    """ Function that convert list in postorder to the arithmetic expression
    Input:
        mylist : list
            Elements to analize and convert
    Output:
        return : str
            Arithmetic expression in string"""

    if not mylist[0] in OPERATORS and len(mylist)==1:
        return str(mylist[0])
    elif len(mylist)==3:
        return str(Node(mylist[2],mylist[0],mylist[1]))
    else:
        for i in range(0,len(mylist)-2):
            if mylist[i+2] in OPERATORS:

                with_simbol=False
                for j in range(0,i+2):
                    if mylist[j] in OPERATORS:
                        with_simbol=True
                        break
                if i-1>0 and not mylist[i-1] in OPERATORS and not(i>0 and not mylist[i] in OPERATORS) and not with_simbol:
                    pass
                else:
                    if not mylist[i] in OPERATORS and not mylist[i+1] in OPERATORS:
                        temp=mylist[i]
                        mylist[i]=str(Node(mylist[i+2],temp,mylist[i+1]))
                        del mylist[i+1]
                        del mylist[i+1]
                        break
        return string_from_postorder(mylist)
