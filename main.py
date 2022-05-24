from implemented_figures import *


def main():
    figures_list = [Triangle(2, 3), Circle(5), Cylinder(5, 10), Cone(5, 10), Sphere(10)]

    for figure in figures_list:
        figure.print_info()


if __name__ == '__main__':
    main()
