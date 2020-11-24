## Implementing __init__() in a superclass

We initialise an object by implementing __init__() method. __init__() method creates the object's instance
variables and performs any other one-time processing.

For example, we create a Card class hierarchy.
We define a Card superclass and three subclasses that are variations of the Card
We have created two instance variables (rank and suit) that have been set directly from argument values,
and two variables (self.hard, self.soft) calculated by an initialization method. (see example class.py)
