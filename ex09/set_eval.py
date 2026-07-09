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


def find_universe(sets):

    all = set()
    for _set in sets:
        for element in _set:
            all.add(element)

    return all


def evaluate(node, sets):

    left_child = ""
    right_child = ""

    if node.data.isalpha():
        return sets[ord(node.data) - 65]

    elif node.data == "!": # change

        universe = find_universe(sets)
        left_child = evaluate(node.left, sets)

        return universe - set(left_child)
    else:
        left_child = evaluate(node.left, sets)
        right_child = evaluate(node.right, sets)
    
    if node.data == "|": # ok
        return (set(left_child) | set(right_child))
    elif node.data == "&": # ok
        return (set(left_child) & set(right_child))
    elif node.data == "^": # ok
        return (set(left_child) ^ set(right_child))
    elif node.data == ">": # change
        universe = find_universe(sets)
        return ((universe - set(left_child)) | right_child)
    elif node.data == "=": # change
        # (A ∧ B) ∨ (!A ∧ !B)

        universe = find_universe(sets)
        comp_left = universe - set(left_child)
        comp_right = universe - set(right_child)

        first_equ = set(left_child) & set(right_child)
        second_equ = comp_left & comp_right

        return first_equ | second_equ



def eval_set(formula: str, sets)-> int:

    _abs = insert(formula)
    result = evaluate(_abs, sets)

    return result



if __name__ == "__main__":

    sets = [{0}, {0}, {0}]

    if check_input("ABC>>"):
        print(eval_set("ABC>>", sets))
    else:
        print("Error: Wrong formula is invalid!")