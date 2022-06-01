from binary_tree import *


def main():
    s1 = Student("Student1", "Surname1", 74, "ir11", 2021)
    s2 = Student("Student2", "Surname2", 89, "ir12", 2021)
    s3 = Student("Student3", "Surname3", 84, "ir13", 2021)
    s4 = Student("Student4", "Surname4", 2, "ir14", 2021)

    root = Node(s1)
    root.insert_node(s2)
    root.insert_node(s3)
    root.insert_node(s4)

    root.print_tree()
    print("=========")
    root.print_nodes_larger_than(s1)


if __name__ == '__main__':
    main()
