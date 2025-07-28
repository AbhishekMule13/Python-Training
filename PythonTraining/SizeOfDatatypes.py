import sys

a = 10
b = 10.5
c = "Abhi"
d = [1, 2, 3]
e = (1, 2)
f = {'name': 'Abhi'}
g = True

print("int:", sys.getsizeof(a), "bytes")
print("float:", sys.getsizeof(b), "bytes")
print("str:", sys.getsizeof(c), "bytes")
print("list:", sys.getsizeof(d), "bytes")
print("tuple:", sys.getsizeof(e), "bytes")
print("dict:", sys.getsizeof(f), "bytes")
print("bool:", sys.getsizeof(g), "bytes")