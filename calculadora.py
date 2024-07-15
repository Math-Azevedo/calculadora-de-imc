import PySimpleGUI as sg

sg.theme('Reddit')

layout = [
    [sg.Text('Informe o peso em kg:'), sg.Input('',size=(6,1), key='peso')],
    [sg.Text('Informe a altura em metro:'), sg.Input('', size=(6,1),key='altura')],
    [sg.Push(), sg.Button('Calcular IMC'), sg.Push()],
    [sg.Text('Resultado IMC:'), sg.Input('', key='resultado_imc', disabled=True)],
    [sg.Text('Categoria IMC:'), sg.Input('', key='categoria_imc', disabled=True)]
]

window = sg.Window('Calculadora IMC', layout=layout, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Calcular IMC':
        try:
            peso = float(values['peso'])
            altura = float(values['altura'])

            imc = peso / (altura * altura)
            imc_text = f'{imc:.2f}'

            if imc < 17.00:
                categoria = 'Muito abaixo do peso'
            elif imc > 17 and imc < 18.50:
                categoria = 'Abaixo do peso'
            elif imc >= 18.51 and imc < 25:
                categoria = 'Peso normal'
            elif imc >= 25 and imc < 30:
                categoria = 'Acima do peso'
            elif imc >= 30 <= imc < 35:
                categoria = 'Obesidade I'
            elif imc >= 35 and imc < 40:
                categoria = 'Obesidade II (severa)'
            else:
                categoria = 'Obesidade III (mórbida)'

            window['resultado_imc'].update(imc_text)
            window['categoria_imc'].update(categoria)

        except ValueError:
            sg.popup('Por favor, insira valores válidos para peso e altura.')

window.close()
