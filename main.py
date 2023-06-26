import tkinter as tk
import pro

def end():
    exit()

def go():
    textin = txtEntry.get()
    if textin == "":
        text = "No Input"
    elif len(textin) > 15:
        text = "Too Long"
    else:
        text = textin
    win.destroy()
    pro.display(text)

win = tk.Tk()
win.title("Turtle Typography!")

txtEntry = tk.Entry(width = 15)
txtEntry.pack()

btnGo = tk.Button(text = "Go!", command = go)
btnGo.pack()

btnExit = tk.Button(text = "Quit", command = end)
btnExit.pack()

win.mainloop()
