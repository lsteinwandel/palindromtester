# Palindromtester von Leo Steinwandel, 14.05.2019

# Importieren der tkinter library
from tkinter import *
from tkinter import ttk
import re

# Funktion zum testen der Eingabe
def palindromtester(x):
    y = x[::-1]
    if len(x) < 2: # Abfrage zur Länge der Eingabe
        return "Bitte wählen sie einen Wort mit mindestens zwei Buchstaben!"
    elif bool(re.match("^[A-Za-z]*$", x)) == 0: # Suche nach verbotenen Symbolen
        return "Bitte geben sie ein gültiges Wort ein"
    elif x.lower() == y.lower(): # Vergleich des Wortes vor- und rückwärts geschrieben
        return "Bei dem Wort " + x + " handelt es sich um ein Palindrom!"
    else:
        return "Das Wort " + x + " ist kein Palindrom!"

# Funktion für den Button
def ergebnis():
    xd = textinput.get()
    text2.config(text=palindromtester(xd))

# Erstellen der graphischen Oberfläche
Ergebnis = ""
gui = Tk() # Erstellen des Fensters
gui.title("Palindromtester von Leo Steinwandel")
gui.geometry("400x100")
gui.resizable(0, 0)
text = ttk.Label(text="Wie lautet das Wort:") # Erstellen des ersten Labels
text.grid()
text.place(x=200, y=20, anchor="center")
textinput = StringVar()
entry = ttk.Entry(textvariable=textinput, width=40) # Erstellen der Texteingabe
entry.grid()
entry.focus()
entry.place(x=200, y=40, anchor="center")
button = ttk.Button(text="Abfrage",command= lambda:ergebnis(),  width=10) # Erstellen des Buttons
button.grid()
button.place(x=200, y=65, anchor="center")
text2 = ttk.Label(text=Ergebnis) # Erstellen des zweiten Labels
text2.grid()
text2.place(x=200, y=90, anchor="center")

# Loopen der GUI
gui.mainloop()