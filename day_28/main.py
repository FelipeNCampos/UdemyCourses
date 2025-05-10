from tkinter import * 
from time import sleep


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
WHITE = "#ffffff"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = 60000

# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def incrementa(c : str):
    hr = int(c.split(":")[0])
    m = int(c.split(":")[1])

    if m < 60:
        m += 1
    if m >= 60:
        m -= 60
        h += 1
    hora = f"{hr:02d}:{m:02d}"
    return hora 


def decrementar(c : str):
    hr = int(c.split(":")[0])
    m = int(c.split(":")[1])

    if hr == 0 and m == 1:
        return "00:00"

    if m > 0:
        m -= 1
    if m <= 0:
        m += 60
        hr -= 1

    hora = f"{hr:02d}:{m:02d}"
    return hora

def addstar():
    temp  = stars.cget(key="text")
    temp += "► "

    stars.config(text=temp)

def start():

    cnv.itemconfig(lbltimer,text="00:"+str(WORK_MIN+1))
    sts.config(text='Work',font=("San Francisco",50))

    contador(WORK_MIN)


def reset():
    temp = ""

    stars.config(text=temp)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

        

def contador(segundos_restantes):
    if segundos_restantes >= 0:
        temp = cnv.itemcget(lbltimer,option="text")
        temp = decrementar(temp)
        cnv.itemconfig(lbltimer,text=temp)
        win.after(TICK, contador, segundos_restantes - 1)
    else:
        if sts.cget(key="text")=="Work":
            addstar()
            sts.config(text='Break',font=("San Francisco",50))
            temp  = stars.cget(key="text")
            if len(temp) >= 8:
                cnv.itemconfig(lbltimer,text="00:"+str(LONG_BREAK_MIN+1))
                contador(LONG_BREAK_MIN)
                reset()

            else:
                cnv.itemconfig(lbltimer,text="00:"+str(SHORT_BREAK_MIN+1))
                contador(SHORT_BREAK_MIN)

        else:
            sts.config(text='Work',font=("San Francisco",50))
            btn_start.grid(row=4,column=0)
            btn_start.config(text="start again")


# ---------------------------- UI SETUP ------------------------------- #


win = Tk()
win.title("Pomodoro")
win.minsize(width=500,height=400)
win.config(background=YELLOW,padx=50,pady=50)

sts = Label(text="Timer",font=("San Francisco",50),background=YELLOW)
sts.grid(row=0,column=1)


cnv = Canvas(width=210,height=224,background=YELLOW)
img = PhotoImage(file="tomato.png")
cnv.create_image(110,112,image=img)


lbltimer = cnv.create_text(110,130,text="00:00",font=("San Francisco",30),fill=WHITE)
cnv.grid(row=1,column=1)



btn_start = Button(text='Start',width=10,font=("San Francisco",15),command=start)
btn_start.grid(row=4,column=0)


stars = Label(text="",font=("San Francisco",15),background=YELLOW)
stars.grid(row=4,column=1)

btn_reset  = Button(text='Reset',width=10,font=("San Francisco",15),command=reset)
btn_reset.grid(row=4,column=2)










win.mainloop()
