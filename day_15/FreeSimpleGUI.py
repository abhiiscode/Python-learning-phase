import day15_def_source_file as functions
import PySimpleGUI as sg
import time
sg.theme("black")

lable = sg.Text("Type in todo to-do")
clock = sg.Text('', key='clock', text_color='pink')

input_box = sg.InputText(tooltip="enter changed name", key="todo", border_width=2)

add_button = sg.Button("Add")
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit", button_color='red')
edit_button = sg.Button("Edit")

list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos', enable_events=False,
                      size=[45, 10])



window = sg.Window('MY to-do app',
                   layout=[[clock],
                          [lable],
                          [input_box, add_button],
                          [list_box, edit_button, complete_button],
                          [exit_button]],

                   font=('helvetica', 10))           # window is : object insest, type
''' in every list inside a list and that list is 1 One row [[ ],[],[]] '''
while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(time.strftime("%A %d - (%b) %m - %Y %H:%M:%S"))
    # print(1, event)
    print(values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values["todo"]
            ''' we use todos because values is is {} Dictionary and that
                content to values in one EX. {'parrot':'Green', "apple":"Red"}
                 And it gives us green, red  '''
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
                break
        case sg.WIN_CLOSED:
            break
window.close()
#
#
# # todos = todos
# # todo = changed_name
# # new_todo = new_todo


# import day12_def_files
# import PySimpleGUI as sg
#
#
# lable1 = sg.Text("Select files to compress:")
# input1 = sg.Input()
# submit_button1 = sg.FilesBrowse("Choose file")
#
# lable2 = sg.Text("Select files to compress:")
# input2 = sg.Input()
# submit_button2 = sg.FilesBrowse("Choose file")
#
# compress_button = sg.Button("compress")
#
#
# window = sg.Window("file compressor",
#                    layout=[[lable1, input1, submit_button1],
#                           [lable2, input2, submit_button2],
#                           [compress_button]])
# while True:
#     event, values = window.read()
#     print(event, values)
# window.close()