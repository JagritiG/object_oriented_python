# example of multiple inheritance


class A:
    def __init__(self):
        self.name1 = "Python"


class B:
    def __init__(self):
        self.name2 = "OOPs"


# child class
class C(A, B):
    def __init__(self):

        # calling constructors of class A and B
        A.__init__(self)
        B.__init__(self)

    def print_name(self):
        print(self.name1, self.name2)


if __name__ == "__main__":

    obj = C()
    obj.print_name()

