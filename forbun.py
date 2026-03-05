from re import X

from pyrsistent import b


fruits = ["apple", "banana", "orange"]

for i in (fruits):
    if i == "banana":
            continue
    print(i)

def sum_list(numbers):
    x=0

    for i in (numbers):
        x = i+x
    return x
numbers = [3, 7, 2, 8]
print(sum_list(numbers))     
    
def sum_list2(numbers2):
    new_list = []
    for i in numbers2:
        new_list.append(i * 2)
    return new_list

numbers2 = [1, 3, 5]
print(sum_list2(numbers2))

def sum_list3(numbers3):
     x =[]
     for i in numbers3:
          if i % 2 == 0:
            x.append(i)
            return x

numbers3 = [1, 2, 3, 4, 5, 6]
print(sum_list3(numbers3))


def sum_list4(numbers4):
    y = []
    for i in numbers4:
        if i < 10:
            y.append(i)
    return y
numbers4 = [3, 12, 7, 20, 1]
print(sum_list4(numbers4))


def sum_list5(numbers5):
    z = []
    for i in numbers5:
        if i % 2 == 0:
            z.append(i)
    return z
numbers5 =[2, 7, 4, 9, 6]
print(sum_list5(numbers5))

