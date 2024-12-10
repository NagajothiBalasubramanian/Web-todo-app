import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass

sg.theme("Black")
clock = sg.Text("",key='clock')
label1=sg.Text("Type a Todo")
input_box=sg.InputText(tooltip="Enter a todo",key="todo")
button1=sg.Button(size=5,image_source='add.png',mouseover_colors='LightGreen',
                  tooltip='Add todo',key="Add")
list_box=sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size=(40,10))
button2=sg.Button("Edit")
button3=sg.Button(size=5,image_source='complete.png',mouseover_colors='lightGreen',
                  tooltip='Delete',key="Delete")
exit_button=sg.Button("Exit")

window=sg.Window('My ToDo App',layout=[[clock],[label1],[input_box,button1],[list_box,button2,button3],
                         [exit_button]],font=('Helvetica','20'))
while True:
    event,values=window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d,%Y %H:%M %S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit",font=('Helvetica',20))

        case "Delete":
            try:
                todo_to_delete = values["todos"][0]
                todos=functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item to delete",font=('Helvetica',20))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()