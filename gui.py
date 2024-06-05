import day15_def_source_file
import FreeSimpleGUI as sg


lable = sg.Text("Type in a to-do")
input_box= sg.InoutText(tooltop="enter todo")

window = sg.Window('to-do ', layout=[[lable], [input_box]])           # window is : object insest, type
window.read()
window.close()

