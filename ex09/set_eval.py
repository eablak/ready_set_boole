from abs import Node, insert

def check_input(input: str) -> bool:

    boolean = 0
    expression = 0

    for char in input:
        if char.isalpha() and char.isupper():
            boolean += 1
        elif char == "&" or char == "|" or char == "^" or char == ">" or char == "=":
            expression += 1

    if (expression+1) == boolean:
        return True
    return False


def evaluate(node, sets):

    left_child = ""
    right_child = ""

    if node.data.isalpha():
        node.data = sets[65 - ord(node.data)]
        return node
    elif node.data == "!":
        left_child = evaluate(node.left, sets)

        globally = []
        for _set in sets:
            for i in _set:
                globally.append(i)

        external = globally.copy()
        for b in left_child.data:
            if b in globally:
                external.remove(b)

        return set(external)
    else:
        left_child = evaluate(node.left, sets)
        right_child = evaluate(node.right, sets)
    
    if node.data == "|":
        return (left_child.data | right_child.data)
    elif node.data == "&":
        return (left_child.data & right_child.data)
    elif node.data == "^":
        return (left_child.data ^ right_child.data)
    elif node.data == ">":

        globally = []
        for _set in sets:
            for i in _set:
                globally.append(i)

        external = globally.copy()
        for b in left_child.data:
            if b in globally:
                external.remove(b)

        return (external | right_child.data)

    elif node.data == "=":

        globally = []
        for _set in sets:
            for i in _set:
                globally.append(i)

        external_left = globally.copy()
        for b in left_child.data:
            if b in globally:
                external_left.remove(b)
        
        left_imp = external_left | right_child.data

        external_right = globally.copy()
        for b in right_child.data:
            if b in globally:
                external_right.remove(b)    

        right_imp = external_right | left_child.data

        return (left_imp & right_imp)
        

def eval_set(formula: str, sets)-> int:

    _abs = insert(formula)
    result = evaluate(_abs, sets)

    return result



if __name__ == "__main__":

    sets = [{42}]

    if check_input("A"):
        print(eval_set("A", sets))
    else:
        print("Error: Wrong formula is invalid!")