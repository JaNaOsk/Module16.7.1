# a={1,2, 3,4}
# b = {'hi', 'hallo', 'hi','hoi', 'bye', 'bye'}
# c=set("abracadabra")
# d= set([1, 2, 3, 4, 2, 5, 6, 6, 6])
# e=set(range(5))
# f=set()
# g=set([[1,2], [2,4]]) unhashible type
# a=[1,2,3,5,5,5,3,4,5,6]
# a=list(set(a))
# a=[1, 2, 3, 4, 2, 5, 6, 6, 6]
# b=[3,7,4,6,9,10]
# c=[]
# for i in a:
#     if i not in b:
#         c.append(i)
# print(a[0],a[-1])

# numbers = input("a:")
#
# numbers_split = numbers.split()
# numbers_lines = "\n".join(numbers_split)
#
# print(numbers_lines)
values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)