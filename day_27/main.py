import tkinter as tk 

window = tk.Tk()
window.title("Miles to KM")
window.minsize(width=500,height=300)


label = tk.Label(text="Im a label")
label.pack()

txtinput = tk.Entry()
txtinput.pack()

label2 = tk.Label(text=txtinput.get())
label2.pack()

def clicked():
    label.config(text="I got clicked")
    label2.config(text=txtinput.get())


button = tk.Button(text="teste",command=clicked)
button.pack()




window.mainloop()

