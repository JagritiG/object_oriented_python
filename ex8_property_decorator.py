# Property Decorator - also known as metaprogrammimg
# Instead of accessing the instance attribute straight, we can define a method that
# returns the attribute and decorate it as a property


# Example-1
# Define a property and the associated getter, setter, deleter method
class Car1:

    def __init__(self):
        self._name = ''

    # using @property decorator
    # getter method
    @property
    def name(self):
        return self._name

    # setter method
    @name.setter
    def name(self, name):
        self._name = name

    # deleter method
    @name.deleter
    def name(self):
        del self._name


# Example-2
# Create class math
class Car:

    # define init method
    def __init__(self):
        self._info = []

    # Property decorator
    # getter method
    @property
    def car_info(self):
        return self._info

    # setter method
    # setter method takes only one value
    @car_info.setter
    def car_info(self, info):
        self._info = info

    # deleter method
    @car_info.deleter
    def car_info(self):
        del self._info


if __name__ == "__main__":

    # example-1
    # create object
    car1 = Car1()

    # set the name
    car1.name = "Honda Accord"

    # get the name
    print(car1.name)

    # delete the name
    del car1.name
    # print(car1.name)

    # Example-2
    car2 = Car()

    # set the info
    car2.car_info = ["Honda Accord", 23000, "2020"]

    # get the name
    print(car2.car_info)

    # delete the info
    del car2.car_info
    # print(car2.car_info)


