import build
build.get_packages()
import tkinter as tk
from tkinter import ttk
from funcs import *
from surveycode import *
from validate import *
import sv_ttk

def submit():

    h=""
    use_digits = nums.get()
    use_symbols = syms.get()
    use_letters = lets.get()
    char_pool = create_char_pool(use_letters, use_digits, use_symbols, forbid.get())
    num = 0
    if char_pool:
        if len_var:
            try:
                num = int(len_var.get())
            except Exception as e:
                print("Error: Please input a valid length")
                cur.config(text="Error: Please input a valid length")
        j=0
        passw=""

        if num > 3:
            print("The length is : " + str(num) + ", The restrictions are: " + forbid.get())
            passw = generate_password(num, char_pool)
            cur.config(text="Generated Password: " + passw)
            score, recs = assess_strength(passw)
            strength_check = "Password Score: "  + str(score) + ", Recommendations: "
            for r in recs:
                strength_check += str(r)
                if r != recs[-1]:
                    strength_check += ", "
            strength.config(text=strength_check)
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

def get_feedback(thanks, show):
    answers = [strong.get(), first.get(), likely.get(), rec.get(), comm.get()]
    df = get_info(answers, username.get())
    thanks.config(text="Thank you! Your response has been recorded.")
    show.config(command=lambda:show_graph(df))
    show.grid(column=1, row=10, stick="w")

def run_survey():
    survey = tk.Toplevel(root)
    survey.title("Welcome to the Password Generator Survey!")
    frame = ttk.Frame(survey, padding=20)
    frame.grid(sticky="nsew")
    frame.grid_rowconfigure(3, minsize=12)
    frame.grid_rowconfigure(5, minsize=12)
    frame.grid_rowconfigure(7, minsize=12)

    thanks = ttk.Label(frame, text="")
    thanks.grid(column=0, row=10, sticky="w")
    show = ttk.Button(frame, text="Show Graph")

    val = (root.register(one_to_five), '%S')
    ttk.Label(frame, text='What is your username or alias?', font=('calibre',10,'normal')).grid(column=0, row=0)
    ttk.Entry(frame, textvariable=username, font=('calibre', 10, 'normal')).grid(column=1, row=0)
    ttk.Checkbutton(frame, text='Was the password strong and secure?', variable=strong, onvalue=1, offvalue=0).grid(column=0, row=1)
    ttk.Checkbutton(frame, text='Is this your first time using a password generator?', variable=first, onvalue=1, offvalue=0).grid(column=0, row=2)

    ttk.Label(frame, text='How likely are you to use this password generator again? (1-5)', font=('calibre',10,'normal')).grid(column=0, row=4)
    ttk.Entry(frame, textvariable=likely, validate='key', validatecommand=val, width=1, font=('calibre', 10, 'normal')).grid(column=1, row=4)
    ttk.Label(frame, text='How likely are you to recommend this password generator to others? (1-5)', font=('calibre',10,'normal')).grid(column=0, row=6)
    ttk.Entry(frame, textvariable=rec, validate='key', validatecommand=val, width=1, font=('calibre', 10, 'normal')).grid(column=1, row=6)
    ttk.Label(frame, text='Any additional comments or feedback?', font=('calibre', 10, 'normal')).grid(column=0, row=8)
    ttk.Entry(frame, textvariable=comm, font=('calibre', 10, 'normal')).grid(column=1, row=8)
    ttk.Button(frame, text='Submit Feedback', command=lambda:get_feedback(thanks, show)).grid(column=0, row=9, padx=10, pady=10)
    ttk.Button(frame, text='Quit', command=survey.destroy).grid(column=1, row=9, padx=10, pady=10)


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Password Generator")
    len_var = tk.StringVar()
    forbid = tk.StringVar()
    lets = tk.IntVar(value=0)
    nums = tk.IntVar(value=0)
    syms = tk.IntVar(value=0)

    username = tk.StringVar()
    strong = tk.IntVar(value=0)
    first = tk.IntVar(value=0)
    likely = tk.StringVar()
    rec = tk.StringVar()
    comm = tk.StringVar()

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
    strength = ttk.Label(frm, text="")
    strength.grid(column=1, row=6, sticky="w")
    ttk.Button(frm, text="Generate Password", command=submit).grid(column=0, row=4, padx=10, pady=10)
    ttk.Button(frm, text="Toggle theme", command=sv_ttk.toggle_theme).grid(column=1, row=4, padx=10, pady=10)
    ttk.Button(frm, text="Take Survey", command=run_survey).grid(column=2, row=4, padx=10, pady=10)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column= 3, row=4, padx=10, pady=10)

    sv_ttk.use_dark_theme()

    root.mainloop()