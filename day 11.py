# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     # for i in grades:
#     #     if i < i:
#     #         print(i)
#     #     else:
#     #         print(None)
#     maximum = max(grades)
#     # print(maximum)
#     return maximum
#
#
# b = get_max()
# print(b)


#2#@#@#@#@#@#@#@#@#@#@#@##@#@#@##@#@@#@#

def get_max():
    grades = [9.6, 9.2, 9.7]
    maxi = max(grades)
    mini = min(grades)
    maximum = f"Mix:{maxi},Min:{mini}"
    return maximum

n = get_max()
print(n)

