import PySimpleGUI as sg

sg.theme("DarkAmber")
sg.set_options(font=("Helvetica", 20), button_element_size=(6, 3))
button_size = (6, 3)
layout = [
    [
        sg.Text(
            "0",
            key="-OUTPUT-",
            size=(10, 3),
            font=("Helvetica", 28),
            justification="right",
            background_color="black",
            text_color="white",
            expand_x=True,
        )
    ],
    [
        sg.Button("C", size=button_size),
        sg.Button("CE", size=button_size),
        sg.Button("Back", size=button_size),
        sg.Button("=", size=button_size),
    ],
    [
        sg.Button("7", size=button_size),
        sg.Button("8", size=button_size),
        sg.Button("9", size=button_size),
        sg.Button("*", size=button_size),
    ],
    [
        sg.Button("4", size=button_size),
        sg.Button("5", size=button_size),
        sg.Button("6", size=button_size),
        sg.Button("/", size=button_size),
    ],
    [
        sg.Button("1", size=button_size),
        sg.Button("2", size=button_size),
        sg.Button("3", size=button_size),
        sg.Button("-", size=button_size),
    ],
    [
        sg.Button("+", size=button_size),
        sg.Button("0", size=button_size),
        sg.Button(".", size=button_size),
        sg.Button("**", size=button_size),
    ],
]

window = sg.Window("Calculator", layout, element_padding=(10, 2))

digits = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in "0123456789.+*/-**":
        digits.append(event)
        print(digits)
        join_digits = "".join(digits)
        window["-OUTPUT-"].update("".join(digits))
        print(join_digits)
    if event == "C":
        digits = []
        window["-OUTPUT-"].update("0")
    if event == "CE":
        digits = []
        window["-OUTPUT-"].update("0")
    if event == "Back":
        digits = digits[:-1]
        window["-OUTPUT-"].update("".join(digits))
    if event == "=":
        window["-OUTPUT-"].update(eval("".join(digits)))
