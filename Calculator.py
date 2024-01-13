import PySimpleGUI as sg
import math

# Definindo o layout da calculadora com as operações adicionais
layout = [
    [sg.Input(size=(30, 1), key='-DISPLAY-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
    [sg.Button('0'), sg.Button('.'), sg.Button('+'), sg.Button('C')],
    [sg.Button(')'), sg.Button('('), sg.Button('sqrt'), sg.Button('**')],
    [sg.Button('=', size=(30, 1))]
]


window = sg.Window('Calculadora Científica', layout)

# Loop para capturar os eventos e realizar os cálculos
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'C':
        window['-DISPLAY-'].update('')
    elif event == '=':
        try:
            expression = values['-DISPLAY-'].replace('sqrt', 'math.sqrt').replace('**', '**')
            result = eval(expression)
            window['-DISPLAY-'].update(result)
        except ValueError:
            window['-DISPLAY-'].update('Erro: Raiz de número negativo')
        except:
            window['-DISPLAY-'].update('Erro')
    else:
        if event in '0123456789.+-*/()sqrt**':
            window['-DISPLAY-'].update(values['-DISPLAY-'] + event)

window.close()