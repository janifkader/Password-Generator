import tkinter as tk
from tkinter import ttk
import sv_ttk
import random

def submit():
    s = ""
    l = ""
    n = ""
    h = ""
    list1=[]
    list2=[]
    list3=[]
    number = nums.get()
    symbol = syms.get()
    letter = lets.get()
    num = int(len_var.get())
    res = forbid.get()
    j=0
    passw=""
    if number:
        list2 = list(range(48, 58))
        while n in res:
            n = chr(random.choice(list2))
        print(n)
        passw += n
        j += 1
    if symbol:
        list3 = list(range(33, 48)) + list(range(91, 97)) + list(range(123, 127))
        while s in res:
            s = chr(random.choice(list3))
        print(s)
        passw += s
        j += 1
    if letter:
        list1 = list(range(65, 91)) + list(range(97, 123))
        while l in res:
            l = chr(random.choice(list1))
        print(l)
        passw += l
        j += 1

    if num != "" and num > 0:
        print("The length is : " + str(num) + ", The restrictions are: " + res)
        listed = list1 + list2 + list3
        for i in range(j, num):
            while h in res:
                h = chr(random.choice(listed))
            print(h)
            passw += h
            h = ""
    else:
        print("Please input a valid length")
    print(passw)
    len_var.set("")
    nums.set(0)
    syms.set(0)
    lets.set(0)
    forbid.set("")

def only_numbers(char):
    return char.isdigit()


root = tk.Tk()
root.iconbitmap('Untitled.ico')
root.title("Password Generator")
len_var=tk.StringVar()
forbid =tk.StringVar()
lets = tk.IntVar()
lets.set(0)
nums = tk.IntVar()
nums.set(0)
syms = tk.IntVar()
syms.set(0)

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Password Length:").grid(column=0, row=0)
valid = (root.register(only_numbers), '%S')
ttk.Entry(frm, textvariable=len_var, validate='key', validatecommand=valid, width=3, font=('calibre',10,'normal')).grid(column=1, row=0)
ttk.Checkbutton(frm, text='Letters?', variable=lets, onvalue=1, offvalue=0).grid(column=0, row=2)
ttk.Checkbutton(frm, text='Numbers?', variable=nums, onvalue=1, offvalue=0).grid(column=1, row=2)
ttk.Checkbutton(frm, text='Symbols?', variable=syms, onvalue=1, offvalue=0).grid(column=2, row=2)
ttk.Label(frm, text="Restrictions:").grid(column=0, row=3)
ttk.Entry(frm, textvariable=forbid, width = 10, font=('calibre',10,'normal')).grid(column=1, row=3)
ttk.Button(frm, text="Generate Password", command=submit).grid(column=0, row=4, padx=10, pady=10)
ttk.Button(frm, text="Toggle theme", command=sv_ttk.toggle_theme).grid(column=1, row=4, padx=10, pady=10)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column= 2, row=4, padx=10, pady=10)

sv_ttk.use_dark_theme()

root.mainloop()