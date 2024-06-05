import day12_def_files
import day15_def_source_file
import PySimpleGUI as sg


lable = sg.Text("Type in todo to-do")
input_box= sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("add")

window = sg.Window('MY to-do app',
                   layout=[[lable],
                   [input_box, add_button]],
                   font=('helvetica', 2))           # window is : object insest, type
''' in every list inside a list and that list is 1 One row [[ ],[],[]] '''
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todo = day15_def_source_file.get_todos()
            new_todo = values["todo"]
            todo.append(new_todo)
            day15_def_source_file.write_todos(todo)
        case sg.WIN_CLOSED():
            break
window.close()


