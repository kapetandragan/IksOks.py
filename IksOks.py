import tkinter as tk
from tkinter import messagebox

def proveri_pobedu():
    # Proveri horizontalne kombinacije
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != "":
            return True

    # Proveri vertikalne kombinacije
    for j in range(3):
        if tabla[0][j] == tabla[1][j] == tabla[2][j] != "":
            return True

    # Proveri dijagonalne kombinacije
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != "":
        return True

    if tabla[0][2] == tabla[1][1] == tabla[2][0] != "":
        return True

    return False

def izvrsi_potez(row, col):
    if tabla[row][col] == "":
        if na_potezu.get() == "X":
            tabla[row][col] = "X"
            buttons[row][col].configure(text="X")
        else:
            tabla[row][col] = "O"
            buttons[row][col].configure(text="O")

        if proveri_pobedu():
            messagebox.showinfo("Kraj igre", f"Pobednik je {na_potezu.get()}")
            resetuj_tablu()
        elif all(tabla[i][j] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Kraj igre", "Nerešeno!")
            resetuj_tablu()
        else:
            na_potezu.set("O" if na_potezu.get() == "X" else "X")

def resetuj_tablu():
    for i in range(3):
        for j in range(3):
            buttons[i][j].configure(text="")
            tabla[i][j] = ""

def napravi_tablu():
    global buttons, tabla
    tabla = [["" for _ in range(3)] for _ in range(3)]
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(root, text="", width=10, height=5, command=lambda x=i, y=j: izvrsi_potez(x, y))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)

root = tk.Tk()
root.title("Iks-Oks")
na_potezu = tk.StringVar()
na_potezu.set("X")

napravi_tablu()

reset_button = tk.Button(root, text="Nova igra", command=resetuj_tablu)
reset_button.grid(row=3, columnspan=3, sticky="we")

root.mainloop()
