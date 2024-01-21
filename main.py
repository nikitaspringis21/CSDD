import PySimpleGUI as sg
from client import Client
from exam import Exam
from transport import Transport

#на чём остановился: 
#    - сделать во втором окне где регистрация на хкамен выбор транспортных средств

sg.theme('DarkBlue2')

categories = ['A', 'A1', 'B', 'B1', 'C', 'D', '95.kods']
car1 = Transport("car", "JR-7201", "Volkswagen", "Golf 7", "diesel", "manual")
transports = []
layout = [
    [sg.Text('Vārds:'), sg.Input(key='name')],
    [sg.Text('Uzvārds:'), sg.Input(key='surname')],
    [sg.Text('Tālrunis:'), sg.Input(key='telNumber')],
    [sg.Text('Dzimšanas datums:'),
     sg.Input(key='birthday', enable_events=True, justification='center'),
     sg.CalendarButton("Izvēlēties datumu", key='calendar_button', format="%Y-%m-%d")],
    [sg.Text('Vēlamā kategorija:'), sg.Combo(categories, key='category', enable_events=True)],
    [sg.Text('Eksāmena tips:'), sg.Radio('Teorijas', 'radio_exam', key='option1', default=True), sg.Radio('Vadīšanas', 'radio_exam', key='option2')],
    [sg.Button('OK')],
]

window = sg.Window('CSDD aplikācija', layout)

def registerForTheory(newClient):
    layout = [
        [sg.Text('Pieraksts teorijas eksāmenam')],
        [sg.Button('OK')],
    ]

    new_window = sg.Window('Pieraksts teorijai', layout)

    while True:
        event, _ = new_window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

    new_window.close()

def registerForDrive(newClient):
    if newClient.category == "B":
        layout = [
            [sg.Text('Vēlamais auto:'), sg.Combo(transports, key='category', enable_events=True)]
        ]

    new_window = sg.Window('Pieraksts braukšanas eksāmenam', layout)

    while True:
        event, _ = new_window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break

    new_window.close()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'OK':
        name = values["name"]
        surname = values["surname"]
        telNumber = values["telNumber"]
        birthday = values["birthday"]
        category = values["category"]
        exam_type = 'Teorijas' if values['option1'] else 'Vadīšanas'
        newClient = Client(name, surname, telNumber, birthday, category, exam_type)
        print(str(newClient))
        window.close()
        if newClient.exam_type == 'Teorijas':
            registerForTheory(newClient)
        elif newClient.exam_type == 'Vadīšanas':
            registerForDrive(newClient)

    elif event == 'Izvēlēties datumu':
        selected_date = sg.popup_get_text('Ievadiet datumu (YYYY-MM-DD)', default_text=values['birthday'])
        if selected_date:
            window['birthday'].update(selected_date)

window.close()
