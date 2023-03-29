from tkinter import Tk, Entry, StringVar, Button, Label
#from pynput.keyboard import Key, Listener

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

def str_wth_comma_to_float(str):
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
    buff=str_wth_comma_to_float(str)

    #buff += float(v.get())
    get_value()
    clean_value()

b1 = Button(root, text="get value", width=10, command=get_value)
b2 = Button(root, text="clean", width=10, command=clean_value)

b1.pack()
b2.pack()

label = Label()
label.pack()

#root.bind('<Control_L>', on_press)
root.bind('<Alt_L>', on_press)


root.mainloop()