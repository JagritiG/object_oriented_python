# Example of polymorphism


# Todo: Example of inbuilt polymorphic functions:
print(len("Python"))    # len() returns length of a string

print(len([1, 2, 3, 4, 5]))  # len() returns length of a list


# Todo: Example of user defined polymorphic function
def add(num1, num2, *args):
    return num1 + num2 + sum(num for num in args)


# Todo: Polymorphism with class methods
# Below code shows how python can use two different class types, in the same way.
# We create a for loop that iterates through a tuple of objects.
# Then call the methods assuming that these methods actually exist in both class.
class Honda:

    def __init__(self):
        self.make = "Honda"
        self.model = "Accord"
        self.status = "Used"

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_status(self):
        return self.status


class Hyundai:

    def __init__(self):
        self.make = "Hyundai"
        self.model = "Palisade"
        self.status = "New"

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_status(self):
        return self.status


# Todo: Polymorphism with Inheritance
# In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
# In inheritance, the child class inherits the methods from the parent class.
# However, it is possible to modify a method in a child class that it has inherited from the parent class.
# This is particularly useful in cases where the method inherited from the parent class does not quite fit the child class.
# In such cases, we re-implement the method in the child class.
# This process of re-implementing a method in the child class is known as Method Overriding.
class Car:

    def __init__(self):
        self.status = "New"
        self.year = "2018"

    def get_year(self):
        return self.year

    def get_status(self):
        return self.status


class Honda1(Car):

    def get_status(self):
        self.status = "Used"
        return self.status


class Hyundai1(Car):

    def get_status(self):
        self.status = "Used"
        return self.status


# Todo: Polymorphism with a Function and objects:


if __name__ == "__main__":

    # Example of user defined polymorphic function
    print(add(2, 3, 5))

    # Polymorphism with class method
    car1 = Honda()
    car2 = Hyundai()
    for info in (car1, car2):
        print(info.get_make())
        print(info.get_model())
        print(info.get_status())

    # Polymorphism with Inheritance
    base_car = Car()
    sub_car1 = Honda1()
    sub_car2 = Hyundai1()

    print(base_car.get_status(), base_car.get_year())
    print(sub_car1.get_status(), base_car.get_year())
    print(sub_car2.get_status(), base_car.get_year())

