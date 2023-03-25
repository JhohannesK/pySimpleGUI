import PySimpleGUI as sg

layout = (
    [
        [sg.Text("Enter minute:", enable_events=True, key="-TEXT-")],
        [sg.InputText(key="-INPUT-")],
        [sg.Button("Convert", key="-CONVERT-")],
        [sg.Text(key="-HELLO-")],
    ],
)

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()
    convertedValue = int(values["-INPUT-"]) * 60
    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        window["-HELLO-"].update("The value in seconds is " + str(convertedValue))

    if event == "-TEXT-":
        print("text has been pressed")

window.close()
