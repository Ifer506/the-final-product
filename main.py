# importing tkinter module
from tkinter import *

root = Tk()

root.geometry("341x541")
root.resizable(0, 0)
root.iconbitmap('cal2.ico')
root.title('Cal 2.0')

# globally declare the expression variable
expressions = ''


def all():
    global expressions
    expressions = ''
    cooling.set('0')


def click(number):
    global expressions

    if number == '1/2':
        expressions = expressions + str('*0.5')
        print(expressions)
        cooling.set(expressions)
        equal_fun()

    elif number == '²':
        p = int(expressions) * int(expressions)
        print(p)
        expressions = str(p)
        cooling.set(expressions)

    elif number == '←':
        e.delete((len(e.get()) - 1), END)
        print(expressions)
        b = int(expressions)
        a = b // 10
        print(a)
        expressions = str(a)
        cooling.set(expressions)

    else:
        expressions = expressions + str(number)
        cooling.set(expressions)

# exception handeling


def equal_fun():
    global expressions
    try:
        total = str(eval(expressions))
        cooling.set(total)
        expressions = ''
        expressions = total
        print(total)
        print(expressions)

    except Exception as u:
        expressions = "Error"
        cooling.set(expressions)
        print(u)
        e.update()


# this create a White frame
f1 = Frame(root, width=35, height=150, highlightbackground="White", highlightthickness=2)
f1.pack(side=TOP)

cooling = StringVar()
e = Entry(f1, width=15, font=('Dubai medium', 31), textvariable=cooling, fg='Black', bg="White", justify=RIGHT)
e.grid(row=0, column=0, ipady=30, columnspan=4)

f2 = Frame(root, width=20, height=10, bg="White")
f2.pack()

b0 = Button(f2, text="0", padx=68, pady=4, fg='black', bg="white", font=("bold", 20), command=lambda: click(0))
b1 = Button(f2, text="1", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(1))
b2 = Button(f2, text="2", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(2))
b3 = Button(f2, text="3", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(3))
b4 = Button(f2, text="4", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(4))
b5 = Button(f2, text="5", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(5))
b6 = Button(f2, text="6", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(6))
b7 = Button(f2, text="7", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(7))
b8 = Button(f2, text="8", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(8))
b9 = Button(f2, text="9", padx=24, pady=7, fg='black', bg="white", font=("bold", 20), command=lambda: click(9))

add = Button(f2, text="+", padx=22, pady=7, fg='gray42', bg="floral white", font=("bold", 20),
             command=lambda: click('+'))
mul = Button(f2, text="x", padx=25, pady=7, fg='gray42', bg="floral white", font=("bold", 20),
             command=lambda: click('*'))
div = Button(f2, text="÷", padx=23, pady=7, fg='gray42', bg="floral white", font=("bold", 20),
             command=lambda: click('/'))
sub = Button(f2, text="-", padx=27, pady=7, fg='gray42', bg="floral white", font=("bold", 20),
             command=lambda: click('-'))
equal = Button(f2, text="=", padx=22, pady=39, fg='gray42', bg="floral white", font=("bold", 20), command=equal_fun)
power = Button(f2, text="x²", padx=66, pady=12, fg='gray42', bg="floral white", font=("bold", 18),
               command=lambda: click('²'))
clear = Button(f2, text="←", padx=17, pady=7, fg='gray42', bg="floral white", font=("bold", 20),
               command=lambda: click('←'))
Ce = Button(f2, text="Ce", padx=62, pady=11, fg='gray42', bg="floral white", font=("bold", 18), command=all)
dec = Button(f2, text=".", padx=27, pady=4, fg='black', bg="white", font=("bold", 20), command=lambda: click('.'))
half = Button(f2, text="½", padx=27, pady=15, fg='gray42', bg="floral white", font=("bold", 15),
              command=lambda: click('1/2'))

# placements
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=0, columnspan=2)

clear.grid(row=1, column=3)
add.grid(row=4, column=3)
equal.grid(row=5, column=3, rowspan=2)
sub.grid(row=1, column=2)
div.grid(row=2, column=3)
mul.grid(row=3, column=3)
power.grid(row=1, column=0, columnspan=2)
Ce.grid(row=6, column=0, columnspan=2)
dec.grid(row=5, column=2)
half.grid(row=6, column=2)

# prevent GUI from closing
root.mainloop()
