import requests

print(f'Модуль requests')
query = {}
response = requests.get("https://yandex.ru")
if response.status_code == 200:
    print(response.text)
    query = response.headers #HTTP-заголовок
    print(query)

import pandas

print(f'Модуль pandas')
file = pandas.read_csv('./testfile.csv')
print(file)
print(file.head(3))
print(file.describe())

import numpy

print(f'Модуль numpy')
a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a.ndim)
print(a.shape)
print(a.size)
print(numpy.zeros((3, 3)))


import matplotlib.pyplot as mp

print(f'Модуль matplotlib')
x = [1, 2, 3, 4, 5]
y = [20, 30, 25, 27, 29]
mp.plot(x, y)
mp.show()


import PIL, пробовал pillow, Но чет не то))
filename = "test.jpg"
with Image.open(filename) as img:
    img.load()
    img.size(800, 600)
    img.save("test1.jpg")

