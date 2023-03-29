from tkinter import Tk, Entry, StringVar, Button, Label
#from pynput.keyboard import Key, Listener
from time import sleep
import keyboard


root = Tk()

v = StringVar()
e = Entry(root, textvariable=v)
e.pack()

buff = 0.0

def get_value():
    #label['text'] = v.get()
    label['text'] = buff

def clean_value():
    v.set("")

def comma_str_to_float(str):
    buff=0
    # find ","
    i = 0
    while str[i] != ',':
        i += 1
        print('i=', i)
    # sum part before ","
    j = 0
    for j in range(i):
        buff += int(str[j]) * (10 ** (i - 1 - j))
        # j+=1
        print('j=', j)
        print("buff=", buff)
    # sum part after ","
    j = 0
    for j in range(1, len(str) - i):
        buff += int(str[i + j]) * (10 ** (-j))
        print('j=', j)
        print("buff=", buff)

    return(buff)

def on_press(key):
    print('{0} release'.format(key))
    global buff
    str = v.get()
    buff=comma_str_to_float(str)

    #buff += float(v.get())
    get_value()
    clean_value()
    #keyboard.send('A')
def on_press2(key):
    keyboard.press("a")
    sleep(1)
    keyboard.release("a")
    print("happend")

def forced_btn_press():
    i=0
    while i!=2:
        #keyboard.press("a")
        sleep(0.5)
        #keyboard.release("a")
        keyboard.send("Ctrl")
        print("happend")
        i+=1


get_value_btn = Button(root, text="get value", width=10, command=get_value)
clean_btn = Button(root, text="clean", width=10, command=clean_value)
start_btn = Button(root, text="start", width=10, command=forced_btn_press)

get_value_btn.pack()
clean_btn.pack()
start_btn.pack()

label = Label()
label.pack()

#root.bind('<Control_L>', on_press)
#keyboard.write("123,456")
#keyboard.send("enter");
root.bind('<Control_L>', on_press)
root.bind('<Shift_L>', on_press2)

root.mainloop()