# Example of Special methods


class SpecialMethod:

    def __init__(self, *args):
        self._list = list(args)

    # special methods
    def __repr__(self):
        """Returns a string object"""
        return repr(self._list)

    def __str__(self):
        """Returns a printable string representation of an object"""
        return str(self._list)

    # Emulating container types
    # Containers usually are sequences (such as lists or tuples) or mappings (like dictionaries),
    def __len__(self):
        """Returns length"""
        return len(self._list)

    def __getitem__(self, key):
        """Called to implement evaluation of self[key].
           the accepted keys should be integers and slice objects
        """
        return self._list[key]

    def __setitem__(self, key, val):
        """Called to implement assignment to self[key]"""
        self._list[key] = val

    def __delitem__(self, key):
        """Called to implement deletion of self[key]"""
        del self._list[key]

    def __iter__(self):
        """Returns return a new iterator object that can iterate over all the objects in the container"""
        return iter(self._list)

    def __contains__(self, item):
        """Returns true if item is in self, false otherwise"""
        return item in self._list

    # Emulating numeric types
    def __add__(self, other):  # also known as operator overloading
        """Called to implement the binary arithmetic operations"""
        return self._list + other._list

    # Emulating callable objects
    def __call__(self, val):
        """Called when the instance is “called” as a function"""
        return self._list[val]


if __name__ == "__main__":

    obj = SpecialMethod("repr", "str", "len", "getitem", "setitem", "iter")
    obj1 = SpecialMethod(1, 3, 5, 6, 7)

    # __repr__()
    print(repr(obj))
    print(obj)

    # __str__()
    print(str(obj))

    # __len__()
    print(len(obj))

    # __getitem__(): key is integer
    print(obj[4])  # output: setitem

    # __getitem__(): keys are slice objects
    print(obj[0:5:3])  # output: ['repr', 'getitem']

    # __setitem__()
    obj[0] = "contains"
    print(obj)          # output: ['contains', 'str', 'len', 'getitem', 'setitem', 'iter']

    # __delitem__()
    del(obj[0])
    print(obj)         # output: ['str', 'len', 'getitem', 'setitem', 'iter']

    # __contains__()
    print("str" in obj)   # output: True

    # __iter__()
    for item in obj:
        print(item)

    # __add_()
    obj2 = SpecialMethod(3, 5, 7)
    print(obj1 + obj2)    # output: [1, 3, 5, 6, 7, 3, 5, 7]
    print(obj + obj2)     # output: ['str', 'len', 'getitem', 'setitem', 'iter', 3, 5, 7]

    # __call__()
    print(obj(0))     # output: str

