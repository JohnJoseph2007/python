from tkinter import messagebox
from tkinter import *
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

def showMessageScreen():
    messagebox.showinfo('Message', 'TEST MESSAGE')

layout = [
    [ps.Text("Calculator")],
    [ps.Text("First Number", size=(12, 1)), ps.InputText(size=(34, 1))],
    [ps.Text("Operator", size=(12, 1)), ps.InputText(size=(34, 1))],
    [ps.Text("Second Number", size=(12, 1)), ps.InputText(size=(34, 1))],
    [ps.Button("Submit",COMMAND=showMessageScreen())]
]
    

window = ps.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event==ps.WIN_CLOSED or event=="Cancel":
        break

window.close()