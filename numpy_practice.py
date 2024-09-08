import numpy

# n = [1, None, False, 'Mohit']        # list
# x = numpy.array(
#     [[1, 2, 3],
#     [4, 2, 3],
#     [1, -2, 66],]
# )

# print(x, type(x))
# print(n, type(n))


# pip install numpy  (NumPy)


a = numpy.array([
    [2, -3],
    [4, 5],
])

b = numpy.array(
    [
        [[1, 2, 3, 4, 5], [2, 3, -0, 2, 5]],
        [[1, 2, 3, 4, 5], [2, 3, 0, 2, 5]],
        [[1, 2, 3, 4, 5], [2, 3, 0, 2, 5]],
    ]
)

# print(a + b)

print(numpy.sin(a))

print(a.shape)

print('--'*20)
print(b.shape)


c = -3 * numpy.ones((3, 5), dtype='int')
print(c)


first_matrix = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
])


second_matrix = numpy.array([
    [7, 8],
    [9, 10],
    [11, 12],
])

third_matrix = numpy.array([
    [2, 2, 2],
    [3, 3, 3]
])


# print(first_matrix * second_matrix)
print(numpy.matmul(first_matrix, second_matrix))

print(first_matrix * third_matrix)


new = numpy.linspace(3, 290, 3)

print('**'*30)
print(new)
print(new.shape)


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    -> 10
# 3, 5

"""
Generating an Array:
 - numpy.array
 - numpy.ones
 - numpy.zeros
 - numpy.arange
 - numpy.linspace

"""


