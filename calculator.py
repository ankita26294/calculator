from tkinter import *


def btnclick(number):
    global val
    val = val + str(number)
    data.set(val)


def btnClear():
    global val
    val = ""
    data.set("")


def btnEquals():
    global val
    result = str(eval(val))
    data.set(result)


root = Tk()
# root var and TK object
root.title("calculator made by Ankita")
root.geometry("361x381+500+200")
val = ""
data = StringVar()
display = Entry(root, textvariable=data, bd=29, justify="right", bg="#DAF7A6", font=("ariel", 20))

display.grid(row=0, columnspan=4)
# create button of numbers
btn7 = Button(root, text="7", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text="+", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick('+'))
btn_add.grid(row=1, column=3)
btn4 = Button(root, text="4", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(6))
btn6.grid(row=2, column=2)
btn_substract = Button(root, text="-", font=("ariel", 12, "bold"), bd=12, height=2, width=6,
                       command=lambda: btnclick('-'))
btn_substract.grid(row=2, column=3)
btn1 = Button(root, text="1", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(3))
btn3.grid(row=3, column=2)
btn_multiply = Button(root, text="*", font=("ariel", 12, "bold"), bd=12, height=2, width=6,
                      command=lambda: btnclick('*'))
btn_multiply.grid(row=3, column=3)
btn_c = Button(root, text="c", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=btnClear)
btn_c.grid(row=4, column=0)
btn0 = Button(root, text="0", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(0))
btn0.grid(row=4, column=1)
btn_division = Button(root, text="/", font=("ariel", 12, "bold"), bd=12, height=2, width=6,
                      command=lambda: btnclick('/'))
btn_division.grid(row=4, column=2)
btn_equal = Button(root, text="=", font=("ariel", 12, "bold"), bd=12, height=2, width=6, command=btnEquals)
btn_equal.grid(row=4, column=3)
root.mainloop()
