- 1. Implementing __init__() in a superclass. We initialise an object by implementing __init__() method. __init__() method creates the object's instance
     variables and performs any other one-time processing. (Example [ex1_init_in_superclass.py](ex1_init_in_superclass.py))

- 2. Example of instance attribute and instance method (Example: [ex2_instance_variable.py](ex2_instance_variable.py))

- 3. Example of initializing subclass using super() (Example: [ex3_initialize_subclass_using_super.py](ex3_initialize_subclass_using_super.py))

- 4. Example of Class Attribute and instance method (Example: [ex4_class_attribute.py](ex4_class_attribute.py))

- 5. Example of Class Method (Example: [ex5_class_method.py](ex5_class_method.py))

- 6. Example of Static Method (Example: [ex6_static_method.py](ex6_static_method.py))

- 7. Difference between @classmethod and @staticmethod:
     - A class method receives the class as implicit first argument,just like an instance method receives the instance.
       A static method does not receive an implicit first argument.
     - A class method can access or modify class state while a static method can’t access or modify it.
     - Static methods know nothing about class state. They are utility type methods that take some parameters
       and work upon those parameters. On the other hand class methods must have class as parameter.
     - We use @classmethod decorator in python to create a class method and we use @staticmethod decorator
       to create a static method in python.
     - We generally use class method to create factory methods. Factory methods return class object
       (similar to a constructor) for different use cases. We generally use static methods to create utility functions.
     - Example: ex5_class_method.py](ex5_class_method.py), [ex6_static_method.py](ex6_static_method.py)

### Properties of @classmethod:
- A class method receives the class as implicit first argument,just like an instance method receives the instance.
- A class method is bound to the class, not to the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class, not to the object instance.
- It can modify a class state that would apply across all the instances of the class.

### Properties of @staticmethod
- A static method does not receive an implicit first argument.
- A static method is also a method which is bound to the class and not the object of the class.
- A static method can’t access or modify class state.
-
