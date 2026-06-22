from abs import Node, insert

def check_input(input: str) -> bool:

    boolean = 0
    expression = 0

    for char in input:
        if char == "1" or char == "0":
            boolean += 1
        elif char == "&" or char == "|" or char == "^" or char == ">" or char == "=":
            expression += 1

    if (expression+1) == boolean:
        return True
    return False


def evaluate(node):

    left_child = ""
    right_child = ""

    if node.data == 0 or node.data == 1:
        return node.data
    elif node.data == "!":
        left_child = evaluate(node.left)
        return not left_child
    else:
        left_child = evaluate(node.left)
        right_child = evaluate(node.right)
    
    if node.data == "|":
        return (left_child | right_child)
    elif node.data == "&":
        return (left_child & right_child)
    elif node.data == "^":
        return (left_child ^ right_child)
    elif node.data == ">":
        return ((not left_child) | right_child)
    elif node.data == "=":
        return (left_child == right_child)
        


def eval_formula(formula: str)-> bool:

    _abs = insert(formula)
    result = evaluate(_abs)

    return result



if __name__ == "__main__":

    input = "1011||="

    if check_input(input):
        print(eval_formula(input))
    else:
        print("Error: Wrong formula is invalid!")