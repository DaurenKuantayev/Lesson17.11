# def func():
#     for i in range(1, 5):
#         print("----------")
#         print("До вызова yield")
#         yield "Вызов yield"
#         print("После вызова yield")
#
#
# a = func()
# print(next(a))
# print(next(a))
# print(next(a))

# a = [1, 2, 3, 4, 5]

# def func(x):
#     print(f'{x} ** 2 = {x ** 2}')
#     return x ** 2

# b = map(func, a)
# print(next(b))
# print(next(b))
# print(next(b))
# b = list(map(func, a))

# b = list(map(lambda x: x ** 2 + 3, a))
# print(b)

aquarium_creatures = [
    {"name": "John", "species": "crab", "tank_number": 23, "type": "shellfish"},
    {"name": "bryan", "species": "shark", "tank_number": 78, "type": "mammal"},
    {"name": "ashley", "species": "lobster", "tank_number": 11, "type": "shellfish"},
    {"name": "bryan", "species": "gold fish", "tank_number": 83, "type": "fish"},
    {"name": "Nemo", "species": "clown fish", "tank_number": 83, "type": "fish"},
]


def change_tank(creatures, new_tank_number):
    def apply(x):
        x["tank_number"] = new_tank_number
        return x
    return map(apply, creatures)

# def apply(x):
#      x["tank_number"] = 35
#     return x

assighned_tanks = change_tank(aquarium_creatures, 35)
print(list(assighned_tanks))

