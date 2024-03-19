my_tuple = (42, "Python", 3.14, "Tuple")

try:
    my_tuple[0] = 10
except TypeError:
    print("Tuples are not mutable")