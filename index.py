import tkinter as tk
from tkinter import * # Tkinter

# class pour connaitre l'operateur
class Calculator():
    def __init__(self): # Construction
        self.phase1 = 0 # Premier nombre
        self.phase2 = 0 # Deuxième nombre
        self.final = 0 # Valeur finale
        self.entry = StringVar() # Capte les valeurs écrit
        self.text = "" # Nombre écrir par l'utilisateur
        self.signe = "" # Type d'opération
        self.entry.set("")
        
    def init(self): # Initialisation 
        self.phase1 = 0 # Premier nombre
        self.phase2 = 0 # Deuxième nombre
        self.final = 0 # Valeur finale
        self.text = "" # Nombre écrir par l'utilisateur
        self.signe = "" # Type d'opération
        
    def afficher_Nb(self): # Afficher les nombre sur écran 
        self.entry.set(self.text)

    def operation(self): # Vérification du type d'opération
        try : 
            if "+" in self.text:
                self.Plus()
            elif "-" in self.text:
                self.Sous()
            elif "/" in self.text:
                self.Div()
            elif "X" in self.text:
                self.Mult()
        except:
            self.entry.set("ERROR")
            self.init()

    def Plus(self): # Addition
        nb = self.text.split("+")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 + self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Sous(self): # Soustraction
        nb = self.text.split("-")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 - self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Div(self): # Division
        nb = self.text.split("/")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 / self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Mult(self): # Multiplication
        nb = self.text.split("X")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 * self.phase2
        self.entry.set(str(self.final))
        self.init()
    
# mes fonctions onclick bouttons
def button0 (): 
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)
    
def button1 ():
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)

def button2 (): 
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)

def button3 ():
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)

def button4 (): 
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)
    
def button5 (): 
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)

def button6 (): 
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)

def button7 (): 
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)

def button8 (): 
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)
    
def button9 (): 
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text)

def Buttonpoint(): 
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)
    
def buttonplus (): 
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)

def buttonmoins (): 
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)

def buttondiviser (): 
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)

def buttonfois ():
    calculatrice.text += "X"
    calculatrice.entry.set(calculatrice.text)

def buttonegal ():
    calculatrice.operation()

def clear (): 
    calculatrice.entry.set("")
    calculatrice.init()
    

window = tk.Tk()

#definition des row et columns
window.rowconfigure([0, 1, 2, 3], minsize=100, weight=1)
window.columnconfigure([0, 1, 2, 3,4], minsize=100, weight=1)


calculatrice = Calculator()
#ou sera ecrit le calcul (input)
ECRAN = Entry(window, width=28, textvariable=calculatrice.entry, fg="black").place(x=9, y=8)

# premiere ligne
btn_decrease = tk.Button(master=window, text="1", command=button1)
btn_decrease.grid(row=1, column=0, sticky="nsew")

btn_decrease = tk.Button(master=window, text="2", command=button2)
btn_decrease.grid(row=1, column=1, sticky="nsew")

btn_decrease = tk.Button(master=window, text="3", command=button3)
btn_decrease.grid(row=1, column=2, sticky="nsew")


# duexieme ligne
btn_decrease = tk.Button(master=window, text="4", command=button4)
btn_decrease.grid(row=2, column=0, sticky="nsew")

btn_decrease = tk.Button(master=window, text="5", command=button5)
btn_decrease.grid(row=2, column=1, sticky="nsew")

btn_decrease = tk.Button(master=window, text="6", command=button6)
btn_decrease.grid(row=2, column=2, sticky="nsew")



# troisieme ligne
btn_decrease = tk.Button(master=window, text="7", command=button7)
btn_decrease.grid(row=3, column=0, sticky="nsew")

btn_decrease = tk.Button(master=window, text="8", command=button8)
btn_decrease.grid(row=3, column=1, sticky="nsew")

btn_decrease = tk.Button(master=window, text="9", command=button9)
btn_decrease.grid(row=3, column=2, sticky="nsew")

frm_entry = tk.Frame(master=window)
lbl_value = tk.Entry(master=frm_entry, width=10)
lbl_value.grid(row=0, column=1, sticky="e")
#lbl_value = tk.Label(master=window, text="0")
#lbl_value.grid(row=0, column=1)



# button operateur 
btn_increase = tk.Button(master=window, text="+", command=buttonplus)
btn_increase.grid(row=0, column=3, sticky="nsew")

btn_increase = tk.Button(master=window, text="-", command=buttonmoins)
btn_increase.grid(row=1, column=3, sticky="nsew")

btn_increase = tk.Button(master=window, text="*", command=buttonfois)
btn_increase.grid(row=2, column=3, sticky="nsew")

btn_increase = tk.Button(master=window, text="/", command=buttondiviser)
btn_increase.grid(row=3, column=3, sticky="nsew")


btn_increase = tk.Button(master=window, text="Clear", command=clear)
btn_increase.grid(row=0, column=4, sticky="nsew")

btn_increase = tk.Button(master=window, text=".", command=Buttonpoint)
btn_increase.grid(row=1, column=4, sticky="nsew")

btn_increase = tk.Button(master=window, text="=", command=buttonegal)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()



#134 juliette dodu