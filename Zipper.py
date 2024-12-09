import FreeSimpleGUI as sg
from Zipcreator import make_archive

label1 = sg.Text("Select files to compress")
input1=sg.Input()
button1 = sg.FilesBrowse("Choose",key="files")

label2 = sg.Text("Select Destination folder")
input2=sg.Input()
button2 = sg.FolderBrowse("Choose",key="folder")

comp_button=sg.Button("Compress")
output = sg.Text(key='output',text_color='Red')

window = sg.Window("File compressor",layout=[[label1,input1,button1],
                                              [label2,input2,button2],
                                             [comp_button,output]])
while True:
    event,values=window.read()
    print(event,values)
    filepaths = values["files"].split(';')
    folder_path=values["folder"]
    make_archive(filepaths,folder_path)
    window['output'].update(value='Compression successful')
window.close()