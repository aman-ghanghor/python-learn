from cgitb import text
from tkinter import *
from tkinter import font
from turtle import right, width

root = Tk()
root.title("Calculator")
root.geometry("361x381+500+200")
display = Entry(root, bd=15, justify="right", bg="powder blue", font=("arial", 20) )
display.grid(row=0, columnspan=4)

# Row 1
btn7 = Button(root, text="7", font=("Arial", 12, "bold"), bd=2, width=4 )
btn7.grid(row=1, column=0)

btn8 = Button(root, text="8", font=("Arial", 12, "bold"), bd=2, width=4 )
btn8.grid(row=1, column=1)

btn9 = Button(root, text="9", font=("Arial", 12, "bold"), bd=2, width=4 )
btn9.grid(row=1, column=2)

btn_add = Button(root, text="+", font=("Arial", 12, "bold"), bd=2, width=4 )
btn_add.grid(row=1, column=3)

# Row 2
btn4 = Button(root, text="4", font=("Arial", 12, "bold"), bd=2, width=4 )
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", font=("Arial", 12, "bold"), bd=2, width=4 )
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", font=("Arial", 12, "bold"), bd=2, width=4 )
btn6.grid(row=2, column=2)

btn_sub = Button(root, text="-", font=("Arial", 12, "bold"), bd=2, width=4 )
btn_sub.grid(row=2, column=3)

# Row 3
btn1 = Button(root, text="1", font=("Arial", 12, "bold"), bd=2, width=4 )
btn1.grid(row=3, column=0)

btn2 = Button(root, text="2", font=("Arial", 12, "bold"), bd=2, width=4 )
btn2.grid(row=3, column=1)

btn3 = Button(root, text="3", font=("Arial", 12, "bold"), bd=2, width=4 )
btn3.grid(row=3, column=2)

btn_mult = Button(root, text="×", font=("Arial", 12, "bold"), bd=2, width=4 )
btn_mult.grid(row=3, column=3)

# Row 4
btn_clr = Button(root, text="c", font=("Arial", 12, "bold"), bd=2, width=4 )
btn_clr.grid(row=4, column=0)

btn0 = Button(root, text="0", font=("Arial", 12, "bold"), bd=2, width=4 )
btn0.grid(row=4, column=1)

btn_div = Button(root, text="÷", font=("Arial", 12, "bold"), bd=2, width=4 )
btn_div.grid(row=4, column=2)

btn_eq = Button(root, text="=", font=("Arial", 12, "bold"), bd=2, width=4 )
btn_eq.grid(row=4, column=3)




root.mainloop()


