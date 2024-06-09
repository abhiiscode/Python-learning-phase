import PySimpleGUI as sg
from zip_creator import make_archive


lable1 = sg.Text("Select files to compress:", text_color="black")
input1 = sg.Input()
submit_button1 = sg.FilesBrowse("Choose", key="files")

lable2 = sg.Text("Select destination folder:", text_color="black")
input2 = sg.Input()
submit_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("compress")
output_lable = sg.Text(key="output", text_color="green")


window = sg.Window("file compressor",
                   layout=[[lable1, input1, submit_button1],
                          [lable2, input2, submit_button2],
                          [compress_button, output_lable]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")
window.close()