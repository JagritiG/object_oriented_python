# Example of single inheritance
# In the following example, we created a superclass Vehicle and three subclasses.
# We factored the __init__() method into the superclass so that a common initialization in the
# superclass, Vehicle, applies to all the three subclasses- Car, Bike.


# Creating Superclass or parent class
class Vehicle:
    def __init__(self, model, price):

        # default constructor
        self.make = "Honda"

        # parameterized constructor
        self.model = model
        self.price = price

    def get_info(self):
        return [self.make, self.model, self.price]


# Creating subclasses or child class
class Car(Vehicle):

    def __init__(self, model, price, status):
        Vehicle.__init__(self, model, price)
        self.status = status

    def get_status(self):
        return self.status


if __name__ == "__main__":
    car1 = Car("Accord", 23000, "used")
    print(car1.get_info(), car1.get_status())











