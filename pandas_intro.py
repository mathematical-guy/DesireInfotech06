import pandas
import random
from matplotlib import pyplot

# pandas.Series  [1, 2, 3, 4]
# pandas.DataFrame  [[2, 3, 4], [2313, 99, -90]]
# list
# list[list]

# garbage_values = [-300]
# proper_values = [random.randint(10, 300) for _ in range(400)]

# values = garbage_values + proper_values + [900]

# x = pandas.Series(values)

# print(x)
# print(type(x))

# [2, 3, -999].

# print(x.std())

# x.plot.pi(color='pink')
# pyplot.show()

# data = {
#   "calories": [420, 380, 390, 1700],
#   "duration": [50, 40, 45, 90],
#   "age": [50, 40, 20, 10]
# }

# data = [
#     [420, 380, 390, 1700],
#     [50, 40, 45, 90],
#     [50, 40, 20, 10]
# ]

# print(pandas.DataFrame(data))


# f = open('datasets/iris.csv')

# print(f.readlines())

# f.close()
# 
# x is a dataframe
x = pandas.read_csv('datasets/iris.csv')
print(x.columns)
x['SepalLengthCm']
# x['SepalLengthCm'].plot.box(color='green')
# x['SepalWidthCm'].plot.box(color='red')
# x['PetalLengthCm'].plot.box()
# x['PetalWidthCm'].plot.box()

# pyplot.show()

# print(x.loc[[46, 51], ['Species', 'SepalLengthCm']])
# x.iloc

# condition = x['Species'] == 'Iris-setosa' | x['Species'] == 'Iris-virginica'
# condition = x['Species'].isin(['Iris-setosa', 'Iris-virginica'])

# condition1 = x['PetalLengthCm'] > 5
# condition2 =  x['Species'].isin(['Iris-setosa'])

# condition = condition2 & condition1

# x.loc[condition1, ['PetalLengthCm', 'PetalWidthCm']] = 5, 3

# print(
#     x.loc[condition1] #, ['PetalWidthCm', 'PetalLengthCm']]
# )

# print(x.describe())

print(x.loc[140:].isnull())