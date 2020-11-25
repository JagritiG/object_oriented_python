# Static Method
# Difference between @classmethdod and @staticmethod: when we call a @classmethod, the class
# is sent as the first argument automatically, but this doen not happen for the @staticmethod.
import datetime

# print(datetime.datetime.now().year)


class Car:

    def __init__(self, name, model, year_built, price):
        self.name = name
        self.model = model
        self.year_built = year_built
        self.price = price

    # a static method to check if a car is new or old car
    @staticmethod
    def is_new(year_built):
        built = datetime.datetime(year_built, 1, 1).year
        current_year = datetime.datetime.now().year
        return "Yes" if built >= current_year else "No"


if __name__ == "__main__":

    # Call static method without instantiating
    print(Car.is_new(2019))
