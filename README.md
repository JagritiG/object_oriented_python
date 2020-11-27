## Object Oriented Python

### Classes and Objects
A class is a user-defined blueprint or prototype from which objects are created. An Object is an instance of a Class.
We initialise an object by implementing __init__() method in Superclass. __init__() method creates the object's instance variables
and performs any other one-time processing. Each class instance have attributes, defined in the class, for maintaining its state.
Class instances also have methods, defined in the class, for modifying its state.

1. Example of Superclass and Subclasses. (Example [ex1_init_in_superclass.py](ex1_init_in_superclass.py))

2. Example of instance attribute and instance method (Example: [ex2_instance_variable.py](ex2_instance_variable.py))

3. Example of initializing subclass using super() (Example: [ex3_initialize_subclass_using_super.py](ex3_initialize_subclass_using_super.py))

4. Example of Class Attribute and instance method (Example: [ex4_class_attribute.py](ex4_class_attribute.py))

5. Example of Class Method (Example: [ex5_class_method.py](ex5_class_method.py))

6. Example of Static Method (Example: [ex6_static_method.py](ex6_static_method.py))

### Properties of Class Attribute (Example: [ex4_class_attribute.py](ex4_class_attribute.py))
- A class attribute is like a global variable of the class which is available to all instances under the class.
- The other benefit is, updating the class attribute updates all the instances of the class.

### Properties of @classmethod: (Example: [ex5_class_method.py](ex5_class_method.py))
- A class method receives the class as implicit first argument,just like an instance method receives the instance.
- A class method is bound to the class, not to the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class, not to the object instance.
- It can modify a class state that would apply across all the instances of the class.

### Properties of @staticmethod (Example: [ex6_static_method.py](ex6_static_method.py))
- A static method does not receive an implicit first argument.
- A static method is also a method which is bound to the class and not the object of the class.
- A static method can’t access or modify class state.

### Difference between @classmethod and @staticmethod:
- A class method receives the class as implicit first argument,just like an instance method receives the instance.
  A static method does not receive an implicit first argument.
- A class method can access or modify class state while a static method can’t access or modify it.
- Static methods know nothing about class state. They are utility type methods that take some parameters
  and work upon those parameters. On the other hand class methods must have class as parameter.
- We use @classmethod decorator in python to create a class method and we use @staticmethod decorator
  to create a static method in python.
- We generally use class method to create factory methods. Factory methods return class object
  (similar to a constructor) for different use cases. We generally use static methods to create utility functions.
- Example: [ex5_class_method.py](ex5_class_method.py), [ex6_static_method.py](ex6_static_method.py)

### Decorators (Example: [ex7_decorator.py](ex7_decorator.py))
- Decorators allow programmers to modify the behavior of the function or class.
- Decorators allow to wrap another function in order to modify the behavior of wrapped function.

### Property Decorator - @property (Example: [ex8_property_decorator.py](ex8_property_decorator.py))
- @property decorator is a built-in python decorator
- Allow to access and modify property attributes of a class using the associated getter, setter, and deleter
- The getter method allows to access the attribute value
- Setter method sets the attribute value. Setter method takes only one value.
- Deleter method deletes the assigned value by the setter method.


### Encapsulation
### Inheritance
### Types of inheritance
### Constructors
### Destructors
### Polymorphism
### Metaprogramming with Metaclass

### Special methods (Example: [ex9_special_methods.py](ex9_special_methods.py)
    See [docs.python.org](https://docs.python.org/3/reference/datamodel.html#specialnames)

- **object.__repr__()**:
  - Called by the repr() built-in function to return a string containing a printable representation of an object.
  - A class can control what this function returns for its instances by defining a __repr__() method.
  - This is used for debugging, so it should be informative.

- **object.__str__()**:
  - Returns a printable string representation of an object
  - This method differs from object.__repr__() in that there is no expectation that __str__() return a valid
    Python expression: a more convenient or concise representation can be used.

**Emulating Container Types
- **object.__len__()**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement the built-in function len()
  - Return the length of the object, an integer >= 0.
  - Also return, an object that doesn’t define a __bool__() method
    and whose __len__() method returns zero is considered to be false in a Boolean context.

- **object.__getitem__(self, key)**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement evaluation of self[key].
  - For sequence types, the accepted keys should be integers and slice objects.
  - Note that the special interpretation of negative indexes (if the class wishes to emulate a sequence type)
    is up to the __getitem__() method.
  - If key is of an inappropriate type, TypeError may be raised;
  - if of a value outside the set of indexes for the sequence (after any special interpretation of negative values),
    IndexError should be raised. For mapping types, if key is missing (not in the container), KeyError should be raised.

- **object.__setitem__(self, key, value)**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement assignment to self[key]. Same note as for __getitem__().
  - This should only be implemented for mappings if the objects support changes to the values for keys,
    or if new keys can be added, or for sequences if elements can be replaced.
  - The same exceptions should be raised for improper key values as for the __getitem__() method.

- **object.__delitem__(self, key)**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement deletion of self[key]. Same note as for __getitem__().
  - This should only be implemented for mappings if the objects support removal of keys,
    or for sequences if elements can be removed from the sequence.
  - The same exceptions should be raised for improper key values as for the __getitem__() method.

- **object.__iter__(self)**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - This method is called when an iterator is required for a container.
  - This method should return a new iterator object that can iterate over all the objects in the container.
  - For mappings, it should iterate over the keys of the container.

**Emulating numeric types**
- **object.__add__(self, other)**:
  - Called to implement the binary arithmetic operation (+)

**Emulating callable objects**
- **object.__call__(self [, args...] )**:
  - Called when the instance is “called” as a function


[Ref: [geekesforgeeks](https://www.geeksforgeeks.org/class-method-vs-static-method-python/?ref=lbp), [medium.com](https://medium.com/@deva.r.p/object-oriented-programming-in-python-a-cheatsheet-7ff4711b9eea)]
