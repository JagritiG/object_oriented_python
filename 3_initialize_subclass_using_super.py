# Create a custom initializer on the sub-class and then call the parent class's initializer via super
# Creating Superclass


class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Create a custom initializer on the sub-class and then call the parent class's initializer via super
# Creating subclasses
class Car(Vehicle):

    def __init__(self, name, price, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        super().__init__(name, price)


if __name__ == "__main__":
    car1 = Car("Honda", 23000, "EX", "2020", "Black")

    print("Vehicle name: {}, price: {}".format(car1.name, car1.price))
    print("Vehicle name: {}, model: {}, year: {}, price: {}, color: {}".format(car1.name, car1.model, car1.year, car1.price, car1.color))

