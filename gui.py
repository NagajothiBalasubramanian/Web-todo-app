import FreeSimpleGUI as sg
import functions

label1=sg.Text("Type a Todo")
input1=sg.InputText(tooltip="Enter a todo",key="todo")
button1=sg.Button("Add")

label2=sg.Text()
input2=sg.InputText()
button2=sg.Button("Edit")

window=sg.Window('My ToDo App',
                 layout=[[label1] ,[input1,button1],
                         [label2,input2,button2]],
                 font=('Helvetica','20'))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()