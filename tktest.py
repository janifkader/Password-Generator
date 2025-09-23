import tkinter as tk
from tkinter import ttk
import sv_ttk
import random
from code import create_char_pool

def submit():

    h=""
    use_digits = nums.get()
    use_symbols = syms.get()
    use_letters = lets.get()
    char_pool = create_char_pool(use_letters, use_digits, use_symbols)
    num = 0
    if char_pool:
        if len_var:
            try:
                num = int(len_var.get())
            except Exception as e:
                print("Error: Please input a valid length")
                cur.config(text="Error: Please input a valid length")
        res = forbid.get()
        j=0
        passw=""

        if num > 3:
            print("The length is : " + str(num) + ", The restrictions are: " + res)
            for i in range(j, num):
                while h in res:
                    h = random.choice(char_pool)
                passw += h
                h = ""
            cur.config(text="Generated Password: " + passw)
        else:
            cur.config(text="Error: Please input a valid length")
        print(passw)
    else:
        cur.config(text="Error: You must select at least one type of character.")
    len_var.set("")
    nums.set(0)
    syms.set(0)
    lets.set(0)
    forbid.set("")

def only_numbers(char):
    return char.isdigit()

if __name__ == "__main__":

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
    cur = ttk.Label(frm, text="")
    cur.grid(column=1, row=5, sticky="w")
    ttk.Button(frm, text="Generate Password", command=submit).grid(column=0, row=4, padx=10, pady=10)
    ttk.Button(frm, text="Toggle theme", command=sv_ttk.toggle_theme).grid(column=1, row=4, padx=10, pady=10)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column= 2, row=4, padx=10, pady=10)

    sv_ttk.use_dark_theme()

    root.mainloop()