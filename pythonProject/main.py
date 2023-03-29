from tkinter import Tk, Entry, StringVar, Button, Label
#from pynput.keyboard import Key, Listener
from time import sleep
import keyboard


root = Tk()

buff = 0.0

def get_value():
    label['text'] = buff

def clean_value(value):
    value.set("")

def comma_str_to_float(str,buff):
    #buff=0
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
    str = main_entry_val.get()
    buff = comma_str_to_float(str, buff)

    #buff += float(v.get())
    get_value()
    clean_value(main_entry_val)
    #keyboard.send('A')
def on_press2(key):
    keyboard.press("a")
    sleep(1)
    keyboard.release("a")
    print("happend")

def forced_btn_press():
    i=0
    global buff
    #while buff != int(f_tr.get())
    while i!=2:
        #keyboard.press("a")
        sleep(0.5)
        #keyboard.release("a")
        keyboard.send("Ctrl")
        print("happend")
        i+=1

#UI
#Сколько сжигаем топлива
fuel_trgr_txt = Label(text="Fuel trigger")
f_tr = StringVar()
fuel_trgr = Entry(root, textvariable=f_tr)
fuel_trgr_txt.grid(row=0, column=0)
fuel_trgr.grid(row=0, column=1)

main_entry_val = StringVar()
main_entry_txt = Label(text="Suda vvodit dannye s vesov")
main_entry = Entry(root, textvariable=main_entry_val)
main_entry.grid(row=1, column=1)
main_entry_txt.grid(row=1, column=0)

#get_value_btn = Button(root, text="get value", width=10, command=get_value)
#clean_btn = Button(root, text="clean", width=10, command=clean_value)
start_btn = Button(root, text="start", width=10, command=forced_btn_press)
start_btn.grid(row=2, column=0,columnspan=3)

#get_value_btn.pack()
#clean_btn.pack()
#start_btn.pack()

label = Label()
label.grid(row=1, column=2)
#label.pack()

#root.bind('<Control_L>', on_press)
#keyboard.write("123,456")
#keyboard.send("enter");
root.bind('<Control_L>', on_press)
root.bind('<Alt_L>', on_press2)

root.mainloop()