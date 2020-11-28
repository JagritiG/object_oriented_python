# Example of destructor
# The _\__del\__()_ method is a known as a destructor method in Python.


class Car:
    def __init__(self, model, price):

        # default constructor
        self.make = "Honda"

        # parameterized constructor
        self.model = model
        self.price = price

    def get_info(self):
        return [self.make, self.model, self.price]

    # Calling destructor for deletion
    def __del__(self):
        print("Car class deleted")


if __name__ == "__main__":
    car1 = Car("Accord", 23000)
    print(car1.get_info())

    # delete the object
    del car1
    print(car1.get_info())     # output: NameError: name 'car1' is not defined

