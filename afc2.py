import time
import random
import threading
import pydirectinput
from tkinter import *
from tkinter import ttk

print("start:")
main1 = 0; #колво окон
stoper = 1; #остановка
tickq = 0;

pydirectinput.FAILSAFE = False


def smooth_move_rel(dx, dy, steps=0, delay=0.0):
    """
    dx, dy — общее смещение по X и Y.
    steps — количество шагов (чем больше, тем плавнее).
    delay — задержка между шагами в секундах.
    """
    step_x = int(dx / steps)
    step_y = int(dy / steps)
    for _ in range(steps):
        if stoper == 1:
            pydirectinput.moveRel(step_x, step_y, relative=True)
            time.sleep(delay)

def main0():
    global tickq
    global main1 
    main1 = 1

    while stoper == 1:
        dx = int(random.uniform(-5000, 5000));
        dy = int(random.uniform(-2000, 2000));

        steps = int(steps1.get());
        delay = float(delay1.get());
        enabl = enabled.get()

        print("сдвиг мыши:", "x:", dx, "y:", dy, "steps:", steps, "delay:", delay, "enabl:", enabl);
        text.insert(END, f"сдвиг мыши: x:{dx} y:{dy}\n Кол-во шагов:{steps}\n Пауза меж шагов:{delay}\n лкм:{enabl}\n")

        smooth_move_rel(dx, dy, steps, delay);
        
        if enabl == 1:
            pydirectinput.click();
        else:
            pass

        tickq += 1;

        print("выполненно.", "Колличество общих завершенных циклов:", tickq)
        text.insert(END, f"Выполненно.\nКоличество завершенных циклов:              {tickq}\n")
    

def main01():
    global main1
    global stoper
    stoper = 1
    main1 += 1
    if main1 == 1:
       thread1 = threading.Thread(target=main0, daemon=True)
       thread1.start()
    else:
        pass	

def main02():
    global main1
    global stoper
    main1 = 0
    stoper = 0

    


def mainn():
    global steps1
    global delay1
    global enabled
    global text

    root = Tk()
    root.title("setings")
    root.geometry("250x300")

    label = ttk.Label(text="__AFK__")
    label.pack()

    label = ttk.Label(text="Кол-во шагов:")
    label.pack()
    steps1 = ttk.Entry(root)
    steps1.pack(padx=6, pady=6)
    steps1.insert(0, "500")

    label = ttk.Label(text="Пауза меж шагов:")
    label.pack()
    delay1 = ttk.Entry()
    delay1.pack(padx=6, pady=6)
    delay1.insert(0, "0.001")

    enabled = IntVar()
    enabled_checkbutton = ttk.Checkbutton(text="Включить нажатие лкм", variable=enabled)
    enabled_checkbutton.pack(padx=6, pady=6)

    btn = ttk.Button(text="seve", command=main01)
    btn.pack(padx=6, pady=6)
    btn = ttk.Button(text="ending", command=main02)
    btn.pack(padx=6, pady=6)

    text = Text(width=30, height=50)
    text.pack()
    text.insert(1.0, "start:\n")
    root.mainloop()

def main():
    thread2 = threading.Thread(target=mainn)
    thread2.start()

main()