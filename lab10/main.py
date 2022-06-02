from binary_tree import *
from student import *


def main():
    students_list = [Student("Oleg", "Bober", 74, "ir11", 2021),
                     Student("Anton", "Tort", 89, "ir12", 2021),
                     Student("Zenovij", "Keks", 84, "ir13", 2021),
                     Student("Andrii", "Gurskiy", 24, "ir14", 2021),
                     Student("Petro", "Sagaidachnyj", 51, "ir11", 2021),
                     Student("Igor", "Neroba", 52, "ir11", 2021),
                     Student("Svyat", "Krtyi", 53, "ir11", 2021)]

    tree = BinaryTree()
    for student in students_list:
        tree.insert(student)

    print("======== all nodes ========")
    tree.print_tree()

    print("======== larger than 53 ========")
    tree.print_nodes_larger_than(students_list[6])

    print("========= after Student5 was deleted ========")
    tree.delete_node(tree.root, students_list[4])
    tree.print_tree()
    tree.delete_all_by_group("ir11")

    print("======== after ir11 was deleted  ========")
    tree = tree.delete_all_by_group("ir11")
    tree.print_tree()
    tree.delete_tree()
    print("======== ======== ======== ========")
    if tree.root is None:
        print("Horray! tree deleted successfully")


if __name__ == '__main__':
    main()
