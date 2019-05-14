# Palindromtester von Leo Steinwandel, 14.05.2019

# Importieren der tkinter library
from tkinter import *
from tkinter import ttk

# Funktion zum testen der Eingabe
def palindromtester(x):
    y = x[::-1]
    if len(x) < 2: # Abfrage zur Länge der Eingabe
        return "Bitte wählen sie einen Namen mit mindestens zwei Buchstaben!"
    elif x.lower() == y.lower(): # Vergleich des Wortes vor- und rückwärts geschrieben
        return "Bei dem Namen " + x + " handelt es sich um ein Palindrom!"
    else:
        return "Der Name " + x + " ist kein Palindrom!"

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
text = ttk.Label(text="Wie lautet der Name:") # Erstellen des ersten Labels
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