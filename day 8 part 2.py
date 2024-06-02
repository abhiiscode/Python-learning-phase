# todos = []
# # file = open(r"C:\Users\Abhi\PycharmProjects\pythonProject\row.txt", 'r') we use "r" for removing \n, \t, \a effect in location path
#
# while True:
#     user_action = input("add, show, edit, remove/complete, all items, or exit : ")
#     user_action = user_action.strip() # use : remove space from input(user_action)
#
#     if 'add' in user_action:
#         # todos = []
           todo = user_action[4:]
#
#         with open('bro.txt', 'r') as file:
#             todos = file.readlines() #   method 2
#
#         # for index, item in enumerate(todos):
#         #     item = item.strip("\n")                # use : to remove ("\n") | # method 3 :for strip ("\n")
#         #     index = index + 1
#         #     row = f"{index}-{item}"        #as well as we can write {index + 1} for start index from 1
#         #     # print(index, item)
#         #     print(row)
#
         todos.append(todo)
#
#
#
#         with open('bro.txt', 'w') as file:
#             file.writelines(todos)
#
#     elif 'show' in user_action:
#
#         with open('bro.txt', 'r') as file:
#             todos = file.readlines()
#
#         for index, item in enumerate(todos):
#             item = item.strip("\n")                # use : to remove ("\n") | # method 3 :for strip ("\n")
#             index = index + 1
#             row = f"{index}-{item}"        #as well as we can write {index + 1} for start index from 1
#             # print(index, item)
#             print(row)
#
#             # with open('bro.txt', 'w') as file:
#             #     file.writelines(todos)
#     elif 'edit' in user_action:
#         number = int(user_action[4:])
#         print(number)
#         number = number - 1
#
#         with open('bro.txt', 'r') as file:
#             todos = file.readlines()
#
#
#         # (only for file "day 8 part 2")print('You choose this word to Edit : ', todos[number])
#         new_char = input("Enter new charecter : ")
#         todos[number] = new_char + '\n'
#        # number = number + 1
#        # (only for file "day 8 part 2") print(number + 1,'replaced by : ',new_char) #in loop we can print index one by one with out using [number = number + 1]
#
#         with open('bro.txt', 'w') as file:
#             file.writelines(todos)  # it will posible in it: file.writelines(['a', 'b', 'c'])
#
#     elif 'complete' in user_action:
#         number = int(user_action[8:])
#
#         with open('bro.txt', 'r') as file:
#             todos = file.readlines()
#         index = number - 1
#         user_remove_item =  todos[index].strip('\n')
#         todos.pop(index)
#
#         with open('bro.txt', 'w') as file:
#             file.writelines(todos)
#
#         message = f"You remove {user_remove_item} form the list."
#         print(message)
#
#     elif 'all items' in user_action:
#         print(len(todos))
#     elif 'exit' in user_action:
#         break
#     else:
#         print("hey you enter a unknown command here please try again")
#
# print("thanx for intracting with us !")
#
