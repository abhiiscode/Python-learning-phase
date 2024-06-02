# def get_age(current_year, year_of_birth):
#     age = current_year - year_of_birth
#     return age
# print(get_age(2024, 2001))

# def get_nr_items(one):
#     split = one.split(" ")
#     cal = [split]
#     return len(cal)
#     # for i in get_nr_items:
#         # print(len(i))
#     return cal
# print(get_nr_items("john, lisa, teresa"))
#
# def get_nr_items(one):
#     split = one.split(",")
#     return len(split)
#
# print(get_nr_items("john, lisa, teresa"))

def get_temp(temperature):
    if input(temperature) > 7:
        return "warm"
    elif input(temperature) <= 7:
        return "cold"
    # return temperature
print(get_temp())

