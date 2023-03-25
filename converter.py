import PySimpleGUI as sg

layout = (
    [
        [
            sg.Text("Choose coversion to perform:", enable_events=True, key="-TEXT-"),
            sg.Combo(["Seconds to Minutes", "Minutes to Seconds"], key="-COMBO-"),
        ],
        [sg.InputText(key="-INPUT-")],
        [sg.Button("Convert", key="-CONVERT-")],
        [sg.Text(key="-HELLO-")],
    ],
)

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        inputValue = values["-INPUT-"]
        if values["-COMBO-"] == "":
            window["-HELLO-"].update("Click the dropdown to select a conversion")
        elif inputValue.isnumeric():
            convertedValuetoSeconds = int(values["-INPUT-"]) * 60
            convertedValuetoMinutes = int(values["-INPUT-"]) / 60
            match values["-COMBO-"]:
                case "Seconds to Minutes":
                    window["-HELLO-"].update(
                        "The value in minutes is " + str(convertedValuetoMinutes)
                    )
                case "Minutes to Seconds":
                    window["-HELLO-"].update(
                        "The value in seconds is " + str(convertedValuetoSeconds)
                    )
        else:
            window["-HELLO-"].update("Please enter a valid number")

    if event == "-TEXT-":
        print("text has been pressed")

window.close()
