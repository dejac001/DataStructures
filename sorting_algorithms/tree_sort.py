"""Sort using a binary tree"""


def sort(my_list: list)-> list:
    from data_structures.trees import BinaryTree
    tree = BinaryTree(my_list[0])
    for i in range(1, len(my_list)):
        tree.add_value(my_list[i])
    return list(tree.sort())
