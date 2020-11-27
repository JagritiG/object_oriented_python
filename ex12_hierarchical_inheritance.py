# Hierarchical Inheritance
# More than one derived classes (child classes) are created from a single parent class


class Car:

    # constructor
    def __init__(self, make):
        self.make = make

    # get brand name
    def get_make(self):
        return self.make


# subclasses or child classes CarA, CarB
class CarA(Car):

    # constructor
    def __init__(self, make, model, year, price):
        Car.__init__(self, make)
        self.model = model
        self.year = year
        self.price = price

    # get info
    def get_info(self):
        return [self.make, self.model, self.year, self.price]


class CarB(Car):

    # constructor
    def __init__(self, make, model, year, price):
        Car.__init__(self, make)
        self.model = model
        self.year = year
        self.price = price

    # get info
    def get_info(self):
        return [self.make, self.model, self.year, self.price]


if __name__ == "__main__":

    car1 = CarA("Honda", "Accord", "2018", 23000)
    car2 = CarB("Hyundai", "Palisade", "2018", 40000)
    print(car1.get_make(), car1.get_info())
    print(car2.get_make(), car2.get_info())
