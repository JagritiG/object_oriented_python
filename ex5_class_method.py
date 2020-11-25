# Class method
# The advantage of class method is - unlike instance methods, we don't
# have to instantiate a class in order to use a class method
# The common use of @classmethod is to instantiate a new object


class Car:

    # Create Class Attribute
    name = "Honda Accord"

    # create instance attribute
    def __init__(self, model, year_built, price):
        self.model = model
        self.year_built = year_built
        self.price = price

    # Define Class Method
    @classmethod
    def get_info(cls):
        return cls.name

    # Define class method to instantiate a new object
    @classmethod
    def get_feature(cls, model, year_built, price):
        return cls(model, year_built, price)


if __name__ == "__main__":

    # Call class method without instantiating
    print(Car.get_info())

    car_info = Car.get_feature("EX", 2020, 24000)
    print(car_info)



