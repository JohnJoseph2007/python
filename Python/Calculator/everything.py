from tkinter.constants import COMMAND
import PySimpleGUI as ps

simpleans = "Nothing yet"

ps.theme("Dark Blue")

def evalsimple(n1, o, n2) :
    global simpleans
    if o == "+":
        simpleans=str(int(n1+n2))
        [ps.Text("Answer is: " + simpleans)]
    elif o == "-":
        simpleans = str(int(n1-n2))
        [ps.Text("Answer is: " + simpleans)]
    elif o == "*":
        simpleans = str(int(n1*n2))
        [ps.Text("Answer is: " + simpleans)]
    elif o == "/":
        simpleans = str(int(n1/n2))
        [ps.Text("Answer is: " + simpleans)]
    elif o == "%":
        simpleans = str(int(n1%n2))
        [ps.Text("Answer is: " + simpleans)]
    else:
        simpleans = "ENTER VALID STUFF PLEASE"
        [ps.Text("Answer is: " + simpleans)]

simpletab = [
    [ps.Text("Basic Arithmetic")],
    [ps.Text("First Number", size=(12, 1)), ps.InputText(size=(34, 1))],
    [ps.Text("Operator", size=(12, 1)), ps.InputText(size=(34, 1))],
    [ps.Text("Second Number", size=(12, 1)), ps.InputText(size=(34, 1))],
    [ps.Button("Submit", COMMAND=showmsgsimple())]
]


areatab = [[ps.Text("Area Arithmetic")]]
sitab = [[ps.Text("Simple Interest Tab")]]
citab = [[ps.Text("Compound Interest Tab")]]

layout = [
    [ps.TabGroup([[
        ps.Tab("Basic Arithmetic", simpletab),
        ps.Tab("Area", areatab),
        ps.Tab("Simple Interest", sitab),
        ps.Tab("Compound Interest", citab)
    ]])]
]

window = ps.Window("Calculator", layout)

while True:
    event, values = window.read()
    print(simpletab[1][1].get())
    print(simpletab[2][1].get())
    print(simpletab[3][1].get())
    if event==ps.WIN_CLOSED or event=="Cancel":
        break

window.close()