# Class Attribute
# We can think of the class attribute as the global variable of the class which is available to all instances under the class.
# Updating the class attribute updates all the instances of the class.


# Define a class attribute
class Car:
    name = "Honda Accord"

    def __init__(self, model, year_built, price):
        self.model = model
        self.year_built = year_built
        self.price = price


if __name__ == "__main__":

    # Access class attribute without instantiating
    print(Car.name)

    # Create two instances
    car1 = Car("EX", "2019", 23000)
    car2 = Car("LX", "2018", 20000)

    # Get class attribute through both instances
    print(car1.name)
    print(car2.name)

    # Change class attribute
    Car.name = "Honda Pilot"

    # Check class attribute through both instances
    print(car1.name)
    print(car2.name)

    # Overwrite the class attribute for each instance
    car1.name = "Honda Civic"
    print(car1.name)

    # Change does not affect the class or other instances
    print(Car.name)
    print(car2.name)
