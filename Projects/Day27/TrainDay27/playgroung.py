# "*args" unlimited arguments

# add(*args):
#     print(args)  # tuple
#     print(type(args))
#     print(sum(args))
#
#
# add(1, 2, 3, 5)
# add(1, 2, 3, 5, 7, 8)


# calculate(n, **kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     # for key, value in kwargs.items():
#     # print(key)
#     # print(value)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


# all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)


# creating a class with many positional keyword arguments ,
# without getting errors with kw.get("make")
# kw["make"] - will throw a KeyError
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("seats")


my_car = Car(make="Nissan")

print(my_car)
print(my_car.model)
