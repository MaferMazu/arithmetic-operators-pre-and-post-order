# :sunny: Arithmetic Operators Pre and Post Order
This is a program that handles arithmetic operations in pre and post order.

## :computer: Requirements

Python3 and pip3.

(opcional) If you want, you can create a virtual environment:

```shell
python3 -m venv env
```

Activate virtual environment:

- Unix/macOS

```shell
source env/bin/activate
```

- Windows

```shell
./env\Script\activate
```

### Install requirements:

```shell
pip3 install -r requirements.txt
```

For install coverage

## :fire: For run it

```shell
python3 main.py
```

## :bulb: How to use it

We have 4 arithmetic operators:

- sum: Represented by the + symbol.

- subtraction: Represented by the symbol -.

- multiplication: Represented by the * symbol.

- integer division: Represented by the / symbol.

And we have 3 commands:

i. EVAL \<order> \<expr>

Represents an evaluation of the expression in \<expr>, which is written according to
to \<order>.
The \<order> can only be:

- PRE: Representing expressions written in pre – fixed order.

- POST: Which represents expressions written in post-fixed order.

For example:

- EVAL PRE + * + 3 4 5 7 should print 42.

- EVAL POST 8 3 - 8 4 4 + * + should print 69.

ii. SHOW \<order> \<expr>

Represents an in-fixed order print of the expression in \<expr>, which is
written according to \<order>.

The \<order> follows the same pattern as in the previous point.

Your program should take the standard precedence and associativity, where:

- Addition and subtraction have the same precedence.

- Multiplication and integer division have the same precedence.

- Integer multiplication and division have higher precedence than addition
and the subtraction.

- All operators associate to left.

The resulting expression should have as few parentheses as possible, so
so that the expression displayed as a result has the same semantics as
the expression that was passed as an argument to the action.

For example:

- SHOW PRE + * + 3 4 5 7 should print (3 + 4) * 5 + 7.

- SHOW POST 8 3 - 8 4 4 + * + should print (8 - 3) + 8 * (4 + 4).

iii. LEAVE

You must exit the program.

## :mag: For run the tests

### Node

```shell
cd tests
coverage3 run --source=node -m unittest test_node.py
coverage3 report -m
```

| Module | Coverage |
|:----:|:--:|
| Node | 100% |

### Formater

```shell
cd tests
coverage3 run --source=formater -m unittest test_formater.py
coverage3 report -m
```

| Module | Coverage |
|:----:|:--:|
| Formater | 91% |

### Main

```shell
cd tests
coverage3 run --source=main -m unittest test_main.py
coverage3 report -m
```

| Module | Coverage |
|:----:|:--:|
| Main | 22% |