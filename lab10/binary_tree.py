# from __future__ import *


class Student:
    def __init__(self, name, surname, rating, group, birth_year) -> None:
        self.name = name
        self.surname = surname
        self.rating = rating
        self.group = group
        self.birth_year = birth_year

    # def __eq__(self, other):
    #     return self.rating == other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __ge__(self, other):
        return self.rating >= other.rating

    def __str__(self):
        return f"Student {self.name} {self.surname} with {self.rating} rating "


class Node:
    def __init__(self, key) -> None:
        self.left_node = None
        self.right_node = None
        self.key = key

    def insert_node(self, key) -> None:
        if self.key is not None:
            if self.key > key:
                if self.left_node is None:
                    self.left_node = Node(key)
                else:
                    self.left_node.insert_node(key)

            elif self.key < key:
                if self.right_node is None:
                    self.right_node = Node(key)
                else:
                    self.right_node.insert_node(key)

    def print_tree(self) -> None:
        if self.left_node:
            self.left_node.print_tree()
        print(f"{self.key}")

        if self.right_node:
            self.right_node.print_tree()

    def print_nodes_larger_than(self, argument) -> None:
        if self.left_node:
            self.left_node.print_nodes_larger_than(argument)

        if self.key >= argument:
            print(f"{self.key}")

        if self.right_node:
            self.right_node.print_nodes_larger_than(argument)

    def search_for_key(self, key) -> int:
        if self.key != key:
            if self.key > key and self.left_node is not None:
                if self.left_node.search_for_key(key):
                    return 1

            elif self.key < key and self.right_node is not None:
                if self.right_node.search_for_key(key):
                    return 1
        else:
            return 1
        return 0

    def delete_node(self, key):
        pass
