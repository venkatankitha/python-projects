import tkinter as tk
from tkinter import font
from tkinter import Label


def get_input(entry, argu):
    entry.insert(tk.END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, tk.END)


def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(tk.END, output)


def popupmsg():
    popup = tk.Tk()
    popup.resizable(0, 0)
    popup.geometry("120x100")
    popup.title("Alert")
    label = tk.Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


def cal():
    root = tk.Tk()
    root.title("Calc")
    root.resizable(0, 0)

    entry_font = font.Font(size=15)
    entry = tk.Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4, sticky=tk.N + tk.W + tk.S + tk.E, padx=5, pady=5)

    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'
    other_button_bg = '#DDDDDD'
    text_fg = '#FFFFFF'
    button_active_bg = '#C0C0C0'

    button7 = tk.Button(root, text='7', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '7'))
    button7.grid(row=2, column=0, pady=5)

    button8 = tk.Button(root, text='8', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '8'))
    button8.grid(row=2, column=1, pady=5)

    button9 = tk.Button(root, text='9', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '9'))
    button9.grid(row=2, column=2, pady=5)

    button10 = tk.Button(root, text='+', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: get_input(entry, '+'))
    button10.grid(row=4, column=3, pady=5)

    button4 = tk.Button(root, text='4', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '4'))
    button4.grid(row=3, column=0, pady=5)

    button5 = tk.Button(root, text='5', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '5'))
    button5.grid(row=3, column=1, pady=5)

    button6 = tk.Button(root, text='6', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '6'))
    button6.grid(row=3, column=2, pady=5)

    button11 = tk.Button(root, text='-', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3, pady=5)

    button1 = tk.Button(root, text='1', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '1'))
    button1.grid(row=4, column=0, pady=5)

    button2 = tk.Button(root, text='2', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '2'))
    button2.grid(row=4, column=1, pady=5)

    button3 = tk.Button(root, text='3', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '3'))
    button3.grid(row=4, column=2, pady=5)

    button0 = tk.Button(root, text='0', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                        command=lambda: get_input(entry, '0'))
    button0.grid(row=5, column=0, pady=5)

    button13 = tk.Button(root, text='.', fg=text_fg, bg=num_button_bg, padx=10, pady=3,
                         command=lambda: get_input(entry, '.'))
    button13.grid(row=5, column=1, pady=5)

    button14 = tk.Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3, pady=5)

    button15 = tk.Button(root, text='<-', fg=text_fg, bg=other_button_bg, padx=10, pady=3,
                         command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=1, column=0, columnspan=2, padx=3, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    button16 = tk.Button(root, text='C', fg=text_fg, bg=other_button_bg, padx=10, pady=3,
                         command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=1, column=2, pady=5)

    button17 = tk.Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=3, pady=5)

    button18 = tk.Button(root, text='^', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                         command=lambda: get_input(entry, '^'))
    button18.grid(row=5, column=2, pady=5)

    exit = tk.Button(root, text='Quit', fg='white', bg='black', command=root.quit, height=1, width=7)
    exit.grid(row=6, column=1)

    root.mainloop()


if __name__ == '__main__':
    cal()
