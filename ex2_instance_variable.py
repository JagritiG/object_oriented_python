# Creating instance variables
class Car:

    # create instance attribute
    def __init__(self, name, model, year_built, price):
        self.name = name
        self.model = model
        self.year_built = year_built
        self.price = price
        self.features = dict()

    # create instance method
    def add_features(self, feature_key, feature_value):
        self.features[feature_key] = feature_value


if __name__ == "__main__":
    car1 = Car("Honda", "EX", 2019, 23000)
    car2 = Car("Honda", "LX", 2020, 20000)

    print("Vehicle name: {}, model: {}, year_built: {}, price: {}".format(car1.name, car1.model, car1.year_built, car1.price))
    print("Vehicle name: {}, model: {}, year_built: {}, price: {}".format(car2.name, car2.model, car2.year_built, car2.price))
    print("Features: {}".format(car1.features))
    print("Features: {}".format(car2.features))

    # Add new features
    car1.add_features("Color", "Black")
    print("Features: {}".format(car1.features))

    car2.add_features("Color", "White")
    print("Features: {}".format(car2.features))


