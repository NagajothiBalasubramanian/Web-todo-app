import FreeSimpleGUI as sg
from convertor import feet_inch_calc

sg.theme('Black')

label1=sg.Text("Enter the Feet")
input1=sg.InputText(key='Feet')

label2=sg.Text("Enter the Inches")
input2=sg.InputText(key='Inches')

convert_button = sg.Button("Convert")
exit_button=sg.Button("Exit")
output_button=sg.Text(key='output')
window = sg.Window('Calculator',layout=[[label1,input1],
                                        [label2,input2],
                                        [convert_button,exit_button,output_button]])

while True:
    event,values=window.read()
    try:
        feet=float(values['Feet'])
        inches=float(values['Inches'])
        meter=feet_inch_calc(feet, inches)
        print(meter)
        window['output'].update(value=f"{meter}m.Converted successfully")
    except ValueError:
        sg.popup("Please enter two numbers")

    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()