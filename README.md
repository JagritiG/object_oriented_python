## Object Oriented Python


1. Example of single inheritance (Example [1_single_inheritance.py](1_single_inheritance.py))

2. Example of instance attribute and instance method (Example: [2_instance_variable.py](2_instance_variable.py))

3. Example of initializing subclass using super() (Example: [3_initialize_subclass_using_super.py](3_initialize_subclass_using_super.py))

4. Example of Class Attribute and instance method (Example: [4_class_attribute.py](4_class_attribute.py))

5. Example of Class Method (Example: [5_class_method.py](5_class_method.py))

6. Example of Static Method (Example: [6_static_method.py](6_static_method.py))

7. Example of Decorator (Example: [7_decorator.py](7_decorator.py))

8. Example of @property decorator (Example: [8_property_decorator.py](8_property_decorator.py))

9. Example of Special Methods (Example: [9_special_methods.py](9_special_methods.py))

10. Example of Multiple inheritance (Example: [10_multiple_inheritance.py](10_multiple_inheritance.py))

11. Example of Multilevel inheritance (Example: [11_multilevel_inheritance.py](11_multilevel_inheritance.py))

12. Example of Hierarchical inheritance (Example: [12_hierarchical_inheritance.py](12_hierarchical_inheritance.py))

13. Example of Private instance variance (Example: [13_private_instance_var.py](13_private_instance_var.py))

14. Example of destructor (Example: [14_destructor.py](14_destructor.py))

15. Example of destructor (Example: [15_polymorphism.py](15_polymorphism.py))

16. Example of Polymorphism - Duck Typing (Example: [16_polymorphism_duck_typing.py](16_polymorphism_duck_typing.py))

17. Example of Polymorphism - Operator Overloading (Example: [17_polymorphism_method_overloading.py](17_polymorphism_method_overloading.py))

18. Example of Polymorphism - Method Overloading (Example: [18_polymorphism_operator_overloading.py](18_polymorphism_operator_overloading.py))

19. Example of Polymorphism - Method Overriding (Example: [19_polymorphism_method_overriding.py](19_polymorphism_method_overriding.py))

20. Example of Metaclass (Example: [20_metaclass.py](20_metaclass.py))

21. Example of Abstraction (Example: [21_abstraction.py](21_abstraction.py))

### Classes and Objects
- A **Class** is a user-defined blueprint or prototype from which objects are created.
- An **Object** is an instance of a Class.
- We initialise an object by implementing _\__init\__()_ method in **Class**.
- _\__init\__()_ method creates the object's instance variables and performs any other one-time processing.
- Each class instance have attributes, defined in the class, for maintaining its state.
- Class instances also have methods, defined in the class, for modifying its state.

### Constructors (Example [1_single_inheritance.py](1_single_inheritance.py))
- We initialise(assign values) an object using Constructors.
- In Python the _\__init\__()_ method is called the constructor and is always called when an object is created.
- _\__init\__()_ method creates the object's instance variables and performs any other one-time processing.
- **Default constructor**: The default constructor does not accept any arguments.
- **Parameterized constructor**: The parameterized constructor accepts arguments.
  The parameterized constructor take _self_ as its first argument and the rest of the arguments are provided by the programmer.

### Destructors (Example: [14_destructor.py](14_destructor.py))
- Destructors are called to destroy an object.
- The _\__del\__()_ method is a known as a destructor method in Python.

### Inheritance
- **Inheritance** is the capability of one class to inherit the properties from another class.
- It is transitive in nature. For example, if class B inherits from class A, then all the
  subclasses of B would automatically inherit from class A.
- **Single inheritance**: When a child class inherits from only one parent class, it is called single inheritance. (Example [1_single_inheritance.py](1_single_inheritance.py))
- **Multiple inheritance**: When a child class inherits from multiple parent classes, it is called multiple inheritance. (Example [10_multiple_inheritance.py](10_multiple_inheritance.py))
- **Multilevel inheritance**: When we have a child and grandchild relationship. (Example [11_multilevel_inheritance.py](11_multilevel_inheritance.py))
- **Hierarchical Inheritance**: More than one derived classes (child classes) are created from a single parent class in hierarchical inheritance. (Example [12_hierarchical_inheritance.py](12_hierarchical_inheritance.py))
- **Private members of parent class**: We can make an instance variable of parent class private by adding double underscores before its name.
  Private instance variables won't be inherited by the child class. (Example [13_private_instance_var.py](13_private_instance_var.py))

### Encapsulation (Example [13_private_instance_var.py](13_private_instance_var.py))
- The action of enclosing something in or as if in a capsule.
- Encapsulation refers to the bundling of data with the methods that operate on that data, or the restricting of direct access
  to some of an object's components.
- The features of encapsulation are supported using classes in most object-oriented languages, although other alternatives also exist.
- To prevent accidental modification of data, an object’s variable can only be changed by an object’s method.
- Those types of object's variables are known as **Private variable**.
- In Python, a variable that is prefixed by **double underscore** is considered as **Private**. (Example [13_private_instance_var.py](13_private_instance_var.py))
- And a variable whose name is prefixed by a **single underscore** is considered **Protected member**.
- **Protected members** are those members of the class that cannot be accessed outside the class but can be accessed from within the class.
  and its subclasses.
- Whereas **Private variable** should neither be accessed outside the class nor by any base class.

### Polymorphism (Example: [15_polymorphism.py](15_polymorphism.py))
- The condition of occurring in several different forms.
- In programming languages and type theory, polymorphism is the provision of a single interface to entities of different types
  or the use of a single symbol to represent multiple different types.
- Python inbuilt polymorphic functions (Example: [15_polymorphism.py](15_polymorphism.py))
- User defined polymorphic function (Example: [15_polymorphism.py](15_polymorphism.py))
- Polymorphism with class methods (Example: [15_polymorphism.py](15_polymorphism.py))
- Polymorphism with inheritance (Example: [15_polymorphism.py](15_polymorphism.py))
- Polymorphism with function and objects (Example: [15_polymorphism.py](15_polymorphism.py))

### Ways of implementing Polymorphism in Python
- Duck Typing (Example: [16_polymorphism_duck_typing.py](16_polymorphism_duck_typing.py))
- Operator Overloading (Example: [17_polymorphism_method_overloading.py](17_polymorphism_method_overloading.py))
- Method Overloading (Example: [18_polymorphism_operator_overloading.py](18_polymorphism_operator_overloading.py))
- Method Overriding (Example: [19_polymorphism_method_overriding.py](19_polymorphism_method_overriding.py))

### Metaprogramming with Metaclass (Example: [20_metaclass.py](20_metaclass.py))

### Abstraction (Example: [21_abstraction.py](21_abstraction.py))

### Properties of Class Attribute (Example: [4_class_attribute.py](4_class_attribute.py))
- A class attribute is like a global variable of the class which is available to all instances under the class.
- The other benefit is, updating the class attribute updates all the instances of the class.

### Properties of @classmethod: (Example: [5_class_method.py](5_class_method.py))
- A class method receives the class as implicit first argument,just like an instance method receives the instance.
- A class method is bound to the class, not to the object of the class.
- They have the access to the state of the class as it takes a class parameter that points to the class, not to the object instance.
- It can modify a class state that would apply across all the instances of the class.

### Properties of @staticmethod (Example: [6_static_method.py](6_static_method.py))
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
- Example: [5_class_method.py](5_class_method.py), [6_static_method.py](6_static_method.py)

### Decorators (Example: [7_decorator.py](7_decorator.py))
- Decorators allow programmers to modify the behavior of the function or class.
- Decorators allow to wrap another function in order to modify the behavior of wrapped function.

### Property Decorator - @property (Example: [8_property_decorator.py](8_property_decorator.py))
- @property decorator is a built-in python decorator
- Allow to access and modify property attributes of a class using the associated getter, setter, and deleter
- The getter method allows to access the attribute value
- Setter method sets the attribute value. Setter method takes only one value.
- Deleter method deletes the assigned value by the setter method.

### Special methods (Example: [9_special_methods.py](9_special_methods.py))
    See [docs.python.org](https://docs.python.org/3/reference/datamodel.html#specialnames)

- **_object.\__repr\__()_**:
  - Called by the repr() built-in function to return a string containing a printable representation of an object.
  - A class can control what this function returns for its instances by defining a _\__repr\__()_ method.
  - This is used for debugging, so it should be informative.

- **_object.\__str\__()_**:
  - Returns a printable string representation of an object
  - This method differs from _object.\__repr\__()_ in that there is no expectation that _\__str\__()_ return a valid
    Python expression: a more convenient or concise representation can be used.

#### Emulating Container Types
- **_object.\__len\__()_**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement the built-in function len()
  - Return the length of the object, an integer >= 0.
  - Also return, an object that doesn’t define a _\__bool\__()_ method
    and whose _\__len\__()_ method returns zero is considered to be false in a Boolean context.

- **_object.\__getitem\__(self, key)_**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement evaluation of self[key].
  - For sequence types, the accepted keys should be integers and slice objects.
  - Note that the special interpretation of negative indexes (if the class wishes to emulate a sequence type)
    is up to the _\__getitem\__()_ method.
  - If key is of an inappropriate type, TypeError may be raised;
  - if of a value outside the set of indexes for the sequence (after any special interpretation of negative values),
    IndexError should be raised. For mapping types, if key is missing (not in the container), KeyError should be raised.

- **_object.\__setitem\__(self, key, value)_**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement assignment to self[key]. Same note as for __getitem__().
  - This should only be implemented for mappings if the objects support changes to the values for keys,
    or if new keys can be added, or for sequences if elements can be replaced.
  - The same exceptions should be raised for improper key values as for the __getitem__() method.

- **_object.\__delitem\__(self, key)_**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - Called to implement deletion of self[key]. Same note as for _\__getitem\__()_.
  - This should only be implemented for mappings if the objects support removal of keys,
    or for sequences if elements can be removed from the sequence.
  - The same exceptions should be raised for improper key values as for the _\__getitem\__()_ method.

- **_object.\__iter\__(self)_**:
  - Defined to implement Container objects such as sequences (such as lists or tuples) or mappings (like dictionaries)
  - This method is called when an iterator is required for a container.
  - This method should return a new iterator object that can iterate over all the objects in the container.
  - For mappings, it should iterate over the keys of the container.

#### Emulating numeric types
- **_object.\__add\__(self, other)_**:
  - Called to implement the binary arithmetic operation (+)

#### Emulating callable objects
- **_object.\__call\__(self [, args...] )_**:
  - Called when the instance is “called” as a function

[Ref: [geekesforgeeks](https://www.geeksforgeeks.org/class-method-vs-static-method-python/?ref=lbp), [medium.com](https://medium.com/@deva.r.p/object-oriented-programming-in-python-a-cheatsheet-7ff4711b9eea), [www.edureka.co](https://www.edureka.co/blog/python-class/#Abstraction)]
