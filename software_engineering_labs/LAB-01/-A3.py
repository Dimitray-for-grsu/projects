from sys import getsizeof

print(getsizeof(3 ** 9090001))
print('It is', int(getsizeof(3 ** 9090001) / 1024), 'kilobytes')
print('It is', round(getsizeof(3 ** 9090001) / 1024 / 1024, 2), 'megabytesbytes')