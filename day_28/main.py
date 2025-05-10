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
TICK = 1000
timer = None

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


    if m > 0:
        m -= 1
    if m <= 0:
        m += 59
        hr -= 1

    if hr < 0:
        return "00:00"
    hora = f"{hr:02d}:{m:02d}"
    return hora

def addstar():
    temp  = stars.cget(key="text")
    temp += "► "

    stars.config(text=temp)

def start():
    global timer 
    cnv.itemconfig(lbltimer,text=f"{WORK_MIN}:00")
    sts.config(text='Work',font=("San Francisco",50),fg=RED)

    timer = contador((WORK_MIN)*60)


def reset():
    temp = ""

    stars.config(text=temp)
    btn_start.config(text="Start")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

        

def contador(segundos_restantes):
    global timer
    if segundos_restantes >= 0:
        temp = cnv.itemcget(lbltimer,option="text")
        temp = decrementar(temp)
        cnv.itemconfig(lbltimer,text=temp)
        win.after(TICK, contador, segundos_restantes - 1)
    else:
        if sts.cget(key="text")=="Work":
            addstar()
            sts.config(text='Break',font=("San Francisco",50),fg=GREEN)
            temp  = stars.cget(key="text")
            if len(temp) >= 8:
                cnv.itemconfig(lbltimer,text=f"{LONG_BREAK_MIN}:00")
                timer = contador((LONG_BREAK_MIN*60)-LONG_BREAK_MIN)
                reset()

            else:
                cnv.itemconfig(lbltimer,text=f"{SHORT_BREAK_MIN}:00")
                timer = contador((SHORT_BREAK_MIN*60)-SHORT_BREAK_MIN)

        else:
            sts.config(text='Work',font=("San Francisco",50))
            btn_start.grid(row=4,column=0)
            btn_start.config(text="Start again")


# ---------------------------- UI SETUP ------------------------------- #


win = Tk()
win.title("Pomodoro")
win.minsize(width=500,height=400)
win.config(background=YELLOW,padx=50,pady=50)

sts = Label(text="Timer",font=("San Francisco",50),background=YELLOW)
sts.grid(row=0,column=1)


cnv = Canvas(width=210,height=224,background=YELLOW,highlightthickness=0)
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
