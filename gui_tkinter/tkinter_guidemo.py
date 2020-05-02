try:
    import tkinter
except ImportError:     # you have python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480")

label = tkinter.Label(mainWindow, text="Hi there!")
label.grid(row=0, column=0)
mainWindow.mainloop()