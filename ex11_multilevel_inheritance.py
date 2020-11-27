# Example of multilevel inheritance
class Car:

    # constructor
    def __init__(self, name, price, year_built):
        self.name = name
        self.price = price
        self.year_built = year_built

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


# subclass or child class of Honda. Grandchild of class Car
class Accord(Honda):

    # constructor
    def __init__(self, name, price, year_built, model, condition):
        Honda.__init__(self, name, price, year_built, model)
        self.condition = condition

    # get condition: new or old
    def get_condition(self):
        return self.condition


if __name__ == "__main__":

    car = Accord("Honda Accord", 23000, "2018", "EX", "New")
    print(car.get_info(), car.get_model(), car.get_condition())
