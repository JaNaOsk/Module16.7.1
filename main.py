# 1 задача
# a=[1,1,2,3,5,8,13,21,34,55,89]
# # b=[]
# for i in a:
#     if i<5:
#         # b.append(i)
#         print(i)
# #2 задача
# a=[1,1,2,3,5,8,13,21,34,55,89]
# b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)
#3 задача
# dict={1:"one", 2:'two',3:"three"}
# dict_1={4:'four',5:'five'}
# dict_2={}
# dict_2.update(dict)
# dict_2.update(dict_1)
# print(dict_2)
# 4 задача
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)

# print(int('ABC', 16))
def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(2)