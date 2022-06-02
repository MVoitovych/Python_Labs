from typing import List


class BinaryTree:
    class Node:
        def __init__(self, key) -> None:
            self.key = key
            self.left_node = None
            self.right_node = None

    def __init__(self) -> None:
        self.root = None

    def insert(self, key) -> None:
        if self.root is None:
            self.root = self.Node(key)
            return

        current_node = self.root
        while current_node and current_node.key != key:
            if current_node.key > key:

                if current_node.left_node is None:
                    current_node.left_node = self.Node(key)
                    return
                else:
                    current_node = current_node.left_node
            elif current_node.key < key:

                if current_node.right_node is None:
                    current_node.right_node = self.Node(key)
                    return
                else:
                    current_node = current_node.right_node

    def find_by_key(self, key) -> bool:
        if self.root is None:
            return False

        current_node = self.root
        while current_node:
            if current_node.key == key:
                return True

            if current_node.key > key:
                current_node = current_node.left_node

            elif current_node.key < key:
                current_node = current_node.right_node

        return False

    def get_tree_in_list(self) -> List:
        key_list = []

        def __get_node_key(current_node) -> None:
            if current_node is None:
                return

            __get_node_key(current_node.left_node)
            __get_node_key(current_node.right_node)

            key_list.append(current_node.key)

        __get_node_key(self.root)
        return key_list

    def __recursive_print(self, current_node) -> None:
        if current_node is None:
            return
        print(current_node.key)
        self.__recursive_print(current_node.right_node)
        self.__recursive_print(current_node.left_node)

    def __recursive_print_nodes_larger_than(self, current_node, key) -> None:
        if current_node is None:
            return

        self.__recursive_print_nodes_larger_than(current_node.right_node, key)
        self.__recursive_print_nodes_larger_than(current_node.left_node, key)
        if current_node.key > key:
            print(current_node.key)

    def print_tree(self) -> None:
        current_node = self.root
        self.__recursive_print(current_node)

    def print_nodes_larger_than(self, key) -> None:
        current_node = self.root
        self.__recursive_print_nodes_larger_than(current_node, key)

    def delete_node(self, current_node, key) -> Node or None:

        if current_node is None:
            return

        if key < current_node.key:
            current_node.left_node = self.delete_node(current_node.left_node, key)

        elif key > current_node.key:
            current_node.right_node = self.delete_node(current_node.right_node, key)

        else:
            if current_node.left_node is None:
                temp_node = current_node.right_node
                return temp_node

            elif current_node.right_node is None:
                temp_node = current_node.left_node
                return temp_node

            temp_node = current_node.right_node

            while temp_node.left_node:
                temp_node = temp_node.left_node
            current_node.key = temp_node.key
            current_node.right_node = self.delete_node(current_node.right_node, temp_node.key)
        return current_node

    def __recursive_delete_node(self, current_node) -> None:
        if current_node is None:
            return
        self.__recursive_delete_node(current_node.left_node)
        self.__recursive_delete_node(current_node.right_node)
        current_node.left_node = None
        current_node.right_node = None

    def delete_tree(self) -> None:
        self.__recursive_delete_node(self.root)
        self.root = None

    def delete_all_by_group(self, group):
        tree_list = self.get_tree_in_list()
        new_tree = BinaryTree()
        for key in tree_list:
            if key.group != group:
                new_tree.insert(key)
        return new_tree
