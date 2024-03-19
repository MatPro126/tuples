my_tuple1 = (1,8)
my_tuple2 = ("Hello", "world")

def swap(a, b):
    (b, a) = (a, b)
    return a, b

print(swap(3, 7))
a, b = my_tuple1
rt1 = (b, a)

a, b = my_tuple2
rt2 = (b, a)

print(rt1,"____",rt2)