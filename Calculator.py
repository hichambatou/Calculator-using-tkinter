import tkinter as tk

# Create window
wind = tk.Tk()

# Set window config
wind.title('Calculator')
wind.config(bg='#2e4a9e')
wind.geometry('400x500')
wind.resizable(False, False)

#Title
title = tk.Label(wind, text='Calculator', font=('Montserrat',20), bg='#002db3', fg='white')
title.place(x=0, y=0, width=400, height=50)

#Box
box = tk.Entry(wind, bd=1, font=('Montserrat',20))
box.place(x=50, y=60, width=300, height=30)

#Functions numbers insert
def button_click(button_number):
    current_number = box.get()
    box.delete(0, tk.END)
    box.insert(0, str(current_number) + str(button_number))

#Clear function
def button_clear():
    box.delete(0, tk.END)

#Addition function
def button_add():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = '+'
    box.delete(0, tk.END)

#Substraction function
def button_substract():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = '-'
    box.delete(0, tk.END)

#Addition function
def button_multiply():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = 'x'
    box.delete(0, tk.END)

#Division function
def button_divide():
    first_number_str = box.get()
    global first_number
    global operation
    first_number = float(first_number_str)
    operation = '÷'
    box.delete(0, tk.END)

#Equal function
def button_equal():
    second_number = float(box.get())
    box.delete(0, tk.END)

    if operation == '+':
      box.insert(0, first_number + second_number)

    elif operation == '-':
      box.insert(0, first_number - second_number)

    elif operation == 'x':
      box.insert(0, first_number * second_number)

    elif operation == '÷':
      box.insert(0, first_number / second_number)

#Define buttons
button_1 = tk.Button(wind, text='1', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(1))
button_2 = tk.Button(wind, text='2', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(2))
button_3 = tk.Button(wind, text='3', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(3))

button_4 = tk.Button(wind, text='4', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(4))
button_5 = tk.Button(wind, text='5', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(5))
button_6 = tk.Button(wind, text='6', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(6))

button_7 = tk.Button(wind, text='7', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(7))
button_8 = tk.Button(wind, text='8', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(8))
button_9 = tk.Button(wind, text='9', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(9))

button_0 = tk.Button(wind, text='0', bd=1, font=('Montserrat',20), bg='#002db3', fg='white', command=lambda: button_click(0))

button_add = tk.Button(wind, text='+', bd=1, font=('Montserrat',20), bg='#4ddbff', fg='black', command=button_add)
button_subtract = tk.Button(wind, text='-', bd=1, font=('Montserrat',20), bg='#4ddbff', fg='black', command=button_substract)
button_multiply = tk.Button(wind, text='x', bd=1, font=('Montserrat',20), bg='#4ddbff', fg='black', command=button_multiply)
button_divide = tk.Button(wind, text='÷', bd=1, font=('Montserrat',20), bg='#4ddbff', fg='black', command=button_divide)

button_equal = tk.Button(wind, text='=', bd=1, font=('Montserrat',20), bg='#000066', fg='white', command=button_equal)
button_clear = tk.Button(wind, text='C', bd=1, font=('Montserrat',20), bg='#000066', fg='white', command = button_clear)

#Show buttons
button_1.place(x=0, y=100, width=100, height=100)
button_2.place(x=100, y=100, width=100, height=100)
button_3.place(x=200, y=100, width=100, height=100)

button_4.place(x=0, y=200, width=100, height=100)
button_5.place(x=100, y=200, width=100, height=100)
button_6.place(x=200, y=200, width=100, height=100)

button_7.place(x=0, y=300, width=100, height=100)
button_8.place(x=100, y=300, width=100, height=100)
button_9.place(x=200, y=300, width=100, height=100)

button_0.place(x=100, y=400, width=100, height=100)

button_clear.place(x=0, y=400, width=100, height=100)
button_equal.place(x=200, y=400, width=100, height=100)

button_add.place(x=300, y=100, width=100, height=100)
button_subtract.place(x=300, y=200, width=100, height=100)
button_multiply.place(x=300, y=300, width=100, height=100)
button_divide.place(x=300, y=400, width=100, height=100)

wind.mainloop()