import FreeSimpleGUI as sg
from convertor import feet_inch_calc

label1=sg.Text("Enter the Feet")
input1=sg.InputText(key='Feet')

label2=sg.Text("Enter the Inches")
input2=sg.InputText(key='Inches')

convert_button = sg.Button("Convert")
output_button=sg.Text(key='output')
window = sg.Window('Calculator',layout=[[label1,input1],
                                        [label2,input2],
                                        [convert_button,output_button]])

while True:
    event,values=window.read()
    feet=float(values['Feet'])
    inches=float(values['Inches'])
    meter=feet_inch_calc(feet, inches)
    print(meter)
    window['output'].update(value=f"{meter}m.Converted successfully")
window.close()