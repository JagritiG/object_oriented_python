# Example of single inheritance
# In the following example, we created a superclass Vehicle and three subclasses.
# We factored the __init__() method into the superclass so that a common initialization in the
# superclass, Vehicle, applies to all the three subclasses- Car, Bike.


# Creating Superclass
class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Creating subclasses
class Car(Vehicle):

    def get_info(self):
        return self.name, self.price


class Bike(Vehicle):

    def get_info(self):
        return self.name, self.price


if __name__ == "__main__":
    vehicle1 = Car("Honda", 23000)
    vehicle2 = Bike("Royal Enfield", 15000)

    print("Vehicle name: {}, price: {}".format(vehicle1.name, vehicle1.price))
    print("Vehicle name: {}, price: {}".format(vehicle2.name, vehicle2.price))







