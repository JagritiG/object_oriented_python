# Example of private instance variable
class Car:

    # constructor
    def __init__(self, name, price, year_built):
        self.name = name
        self.price = price
        self.year_built = year_built

        # create private variable
        self.__dealer = "GoCar"

    # to get name
    def get_info(self):
        return [self.name, self.price, self.year_built]


# subclass or child class
class Honda(Car):

    # constructor
    def __init__(self, name, price, year_built, model):
        Car.__init__(self, name, price, year_built)
        self.model = model

    # get honda info
    def get_model(self):
        return self.model


if __name__ == "__main__":

    # create object of child class Honda
    honda = Honda("Honda Accord", 23000, "2018", "EX")

    # Accessing instance variables of parent class Car
    print(honda.get_info(), honda.get_model())

    # Accessing private instance variable of parent class
    print(honda.__dealer)   # output: AttributeError: 'Honda' object has no attribute '__dealer'
