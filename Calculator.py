import tkinter as tk
import tkinter.font as font

#global variables
root =tk.Tk()
root.title("Calculator")
root.geometry("700x600")
myFont = font.Font(size=40, weight="bold")

#Building the expression

expression = ""
equation = tk.StringVar() 
equation.set(' 0')

def ExpBuild(press):
    global expression
    expression = expression + str(press)
    equation.set(expression) 

def Calc():
    try:
        global expression
        equation.set(str(eval(expression)))
    except:
        equation.set("Math Error")
        
def clear():
    global expression
    global equation 
    equation.set(" 0")
    expression = ""


#Declaring Frame,Label,button etc. from main root

frame = tk.Frame(root, bg= '#80c1ff')
frame.place(relx=0, rely=0.2, relwidth=0.8, relheight=0.7)

label = tk.Label(root, text="Abraham's Calculator", bg='#116466')
label.place(relx=0, rely=0, relwidth=1, relheight=0.05)
label['font'] = font.Font(size=22)

equal = tk.Button(root, text="=", bg='#2c3531', fg='#116466', command=Calc)
equal.place(relx=0, rely=0.9, relwidth=0.8, relheight=0.1)
equal['font'] = font.Font(size=40)

equal = tk.Button(root, text="Clear", bg='#2c3531', fg='#116466', command=clear)
equal.place(relx=0.8, rely=0.9, relwidth=0.2, relheight=0.1)
equal['font'] = font.Font(size=22)

entry = tk.Entry(root, bg="#2c3531", textvariable=equation)
entry.place(relx=0, rely=.05, relwidth=1 ,relheight= 0.15)
entry['font'] = myFont



oper = tk.Frame(root, bg= '#80c1ff')
oper.place(relx=0.8, rely=0.2, relwidth=0.2, relheight=0.7)



#Declaring Buttons in frame oper

buttondiv = tk.Button(oper, text="/", bg='#2c3531', fg='#116466', command=lambda: ExpBuild("/"))
buttondiv.place(relx=0, rely=0, relheight = 0.25, relwidth=1)
buttondiv['font'] = myFont

buttonmul = tk.Button(oper, text="*", bg='#2c3531', fg='#116466', command=lambda: ExpBuild("*"))
buttonmul.place(relx=0, rely=0.25, relheight = 0.25, relwidth=1)
buttonmul['font'] = myFont

buttonsub = tk.Button(oper, text="-", bg='#2c3531', fg='#116466', command=lambda: ExpBuild("-"))
buttonsub.place(relx=0, rely=0.5, relheight = 0.25, relwidth=1)
buttonsub['font'] = myFont

buttonadd = tk.Button(oper, text="+", bg='#2c3531', fg='#116466', command=lambda: ExpBuild("+"))
buttonadd.place(relx=0, rely=0.75, relheight = 0.25, relwidth=1)
buttonadd['font'] = myFont





#Declaring Buttons from frame, frame

button7 = tk.Button(frame, text="7", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(7))
button7.place(relx=0, rely=0, relheight = 0.25, relwidth=1/3)
button7['font'] = myFont

button8 = tk.Button(frame, text="8", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(8))
button8.place(relx=0.33, rely=0, relheight = 0.25, relwidth=1/3)
button8['font'] = myFont

button9 = tk.Button(frame, text="9", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(9))
button9.place(relx=0.66, rely=0, relheight = 0.25, relwidth=0.34)
button9['font'] = myFont

button6 = tk.Button(frame, text="4", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(4))
button6.place(relx=0, rely=0.25, relheight = 0.25, relwidth=0.33)
button6['font'] = myFont

button5 = tk.Button(frame, text="5", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(5))
button5.place(relx=0.33, rely=0.25, relheight = 0.25, relwidth=0.33)
button5['font'] = myFont

button4 = tk.Button(frame, text="6", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(6))
button4.place(relx=0.66, rely=0.25, relheight = 0.25, relwidth=0.34)
button4['font'] = myFont

button3 = tk.Button(frame, text="1", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(1))
button3.place(relx=0, rely=0.50, relheight = 0.25, relwidth=0.33)
button3['font'] = myFont

button2 = tk.Button(frame, text="2", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(2))
button2.place(relx=0.33, rely=0.50, relheight = 0.25, relwidth=0.33)
button2['font'] = myFont

button1 = tk.Button(frame, text="3", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(3))
button1.place(relx=0.66, rely=0.50, relheight = 0.25, relwidth=0.34)
button1['font'] = myFont

button0 = tk.Button(frame, text="0", bg='#2c3531', fg='#116466', command=lambda: ExpBuild(0))
button0.place(relx=0, rely=0.75, relheight = 0.25, relwidth=0.66)
button0['font'] = myFont

buttondec = tk.Button(frame, text=".", bg='#2c3531', fg='#116466', command=lambda: ExpBuild("."))
buttondec.place(relx=0.66, rely=0.75, relheight = 0.25, relwidth=0.34)
buttondec['font'] = myFont




root.mainloop()
