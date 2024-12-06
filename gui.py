import FreeSimpleGUI as sg

label=sg.Text("Type a Todo")
input1=sg.InputText(tooltip="Enter a todo")
button1=sg.Button("Add")

window=sg.Window('My ToDo App',layout=[[label ,input1,button1]])
window.read()
print("Hello")
window.close()