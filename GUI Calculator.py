#importing modules to be used
import tkinter
import math
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button

expression = "" 
  
#defining functions to enter,evaluate,clear screen;calculator functions  
def enter(num): 
    global expression
    expression = expression + str(num) 

    equation.set(expression) 
    
def equalto(): 
    try: 
  
        global expression 
  
        total = str(eval(expression))   
        equation.set(total)   
        expression = "" 
   
    except: 
  
        equation.set("Error") 
        expression = "" 
    
def clrscr(): 
    global expression 

    expression = "" 
    equation.set("")

def fact():
    try:
        global expression

        exp=float(expression)
        pro=str(math.factorial(exp))
        equation.set(pro)
        expression=""
    
    except:
        
        equation.set("Error")
        expression=""

def root():
    global expression
    
    x=float(expression)
    sqroot=str(math.sqrt(x))
    equation.set(sqroot)
    expression=""
    
def sine():
    global expression
    
    x=float(expression)
    si=str(math.sin(x))
    equation.set(si)
    expression=""
    
def cosine():
    global expression
    
    x=float(expression)
    co=str(math.cos(x))
    equation.set(co)
    expression=""

def tangent():
    global expression
    
    x=float(expression)
    ta=str(math.tan(x))
    equation.set(ta)
    expression=""
    
def sineh():
    global expression
    
    x=float(expression)
    sih=str(math.sinh(x))
    equation.set(sih)
    expression=""
    
def cosineh():
    global expression
    
    x=float(expression)
    coh=str(math.cosh(x))
    equation.set(coh)
    expression=""

def tangenth():
    global expression
    
    x=float(expression)
    tah=str(math.tanh(x))
    equation.set(tah)
    expression=""    

  
if __name__=="__main__":

#making basic window using tkinter
    gui=tkinter.Tk()
    equation=StringVar()

#defining basic window's dimensions,etc. 
    gui.configure(background="grey")
    gui.title('Simple Calculator')
    gui.geometry('375x200')
        
#setting the entry box for user input
    text_ip=Entry(gui,justify='left'
                  ,textvariable=equation)
    text_ip.grid(columnspan=5, ipadx=75)
    
    equation.set('')

#setting buttons on the calculator    
    button1= Button(gui,text='1',fg='white',bg='blue',
                    command=lambda: enter(1),height=1,width=7,
                    activebackground='powder blue')
    button1.grid(row=2,column=0)
    
    button2= Button(gui,text='2',fg='white',bg='blue',
                    command=lambda: enter(2),height=1,width=7,
                    activebackground='powder blue')
    button2.grid(row=2,column=1)
    
    button3= Button(gui,text='3',fg='white',bg='blue',
                    command=lambda: enter(3),height=1,width=7,
                    activebackground='powder blue')
    button3.grid(row=2,column=2)
    
    button4= Button(gui,text='4',fg='white',bg='blue',
                    command=lambda: enter(4),height=1,width=7,
                    activebackground='powder blue')
    button4.grid(row=3,column=0)
    
    button5= Button(gui,text='5',fg='white',bg='blue',
                    command=lambda: enter(5),height=1,width=7,
                    activebackground='powder blue')
    button5.grid(row=3,column=1)
    
    button6= Button(gui,text='6',fg='white',bg='blue',
                    command=lambda: enter(6),height=1,width=7,
                    activebackground='powder blue')
    button6.grid(row=3,column=2)
    
    button7= Button(gui,text='7',fg='white',bg='blue',
                    command=lambda: enter(7),height=1,width=7,
                    activebackground='powder blue')
    button7.grid(row=4,column=0)
    
    button8= Button(gui,text='8',fg='white',bg='blue',
                    command=lambda: enter(8),height=1,width=7,
                    activebackground='powder blue')
    button8.grid(row=4,column=1)
    
    button9= Button(gui,text='9',fg='white',bg='blue',
                    command=lambda: enter(9),height=1,width=7,
                    activebackground='powder blue')
    button9.grid(row=4,column=2)
    
    button0= Button(gui,text='0',fg='white',bg='blue',
                    command=lambda: enter(0),height=1,width=7,
                    activebackground='powder blue')
    button0.grid(row=5,column=0)
    
    dot= Button(gui,text='.',fg='white',bg='blue',
                command=lambda: enter("."),height=1,width=7,
                activebackground='powder blue')
    dot.grid(row=5,column=1)
    
    equal= Button(gui,text='=',fg='white',bg='blue',
                  command=equalto,height=1,width=7,
                  activebackground='powder blue')
    equal.grid(row=5,column=2)
    
    plus= Button(gui,text='+',fg='white',bg='blue',
                 command=lambda: enter("+"),height=1,width=7,
                 activebackground='powder blue')
    plus.grid(row=2,column=3)
    
    minus= Button(gui,text='-',fg='white',bg='blue',
                  command=lambda: enter("-"),height=1,width=7,
                  activebackground='powder blue')
    minus.grid(row=3,column=3)
    
    mult= Button(gui,text='*',fg='white',bg='blue',
                 command=lambda: enter("*"),height=1,width=7,
                 activebackground='powder blue')
    mult.grid(row=4,column=3)
    
    div= Button(gui,text='/',fg='white',bg='blue',
                command=lambda: enter("/"),height=1,width=7,
                activebackground='powder blue')
    div.grid(row=5,column=3)
    
    clear= Button(gui,text='AC',fg='black',bg='dark orange',
                  command=clrscr,height=1,width=7,
                  activebackground='powder blue')
    clear.grid(row=2,column=5)
    
    facto= Button(gui,text='Factorial',fg='black',bg='white',
                  command=fact,height=1,width=7,
                  activebackground='powder blue')
    facto.grid(row=3,column=4)
    
    sqr= Button(gui,text='Root',fg='black',bg='white',
                command=root,height=1,width=7,
                activebackground='powder blue')
    sqr.grid(row=4,column=4)
    
    exp= Button(gui,text='**',fg='black',bg='white',
                command=lambda: enter("**"),height=1,width=7,
                activebackground='powder blue')
    exp.grid(row=5,column=4)
    
    msine= Button(gui,text='sine()',fg='white',bg='black',
                  command=sine,height=1,width=7
                  ,activebackground='powder blue')
    msine.grid(row=6,column=0)
    
    mcos= Button(gui,text='cos()',fg='white',bg='black',
                  command=cosine,height=1,width=7,
                  activebackground='powder blue')
    mcos.grid(row=6,column=1)
    
    mtan= Button(gui,text='tan()',fg='white',bg='black',
                  command=tangent,height=1,width=7
                  ,activebackground='powder blue')
    mtan.grid(row=6,column=2)  
    
    msinh= Button(gui,text='sinh()',fg='white',bg='black',
                  command=sineh,height=1,width=7,
                  activebackground='powder blue')
    msinh.grid(row=7,column=0)
    
    mcosh= Button(gui,text='cosh()',fg='white',bg='black',
                  command=cosineh,height=1,width=7,
                  activebackground='powder blue')
    mcosh.grid(row=7,column=1)
    
    mtanh= Button(gui,text='tanh()',fg='white',bg='black',
                  command=tangenth,height=1,width=7,
                  activebackground='powder blue')
    mtanh.grid(row=7,column=2)
    
    vpi= Button(gui,text='π',fg='white',bg='red',
                command=lambda: enter(3.14159),height=1,width=4,
                activebackground='powder blue')
    vpi.grid(row=3,column=5)
    
    ve= Button(gui,text='e',fg='white',bg='red',
               command=lambda: enter(2.71828),height=1,width=4,
               activebackground='powder blue')
    ve.grid(row=4,column=5)
    
    brack1= Button(gui,text='(',fg='black',bg='yellow',
                   command=lambda: enter("("),height=1,width=2,
                   activebackground='powder blue')
    brack1.grid(row=5,column=5)
    brack2= Button(gui,text=')',fg='black',bg='yellow',
                   command=lambda: enter(")"),height=1,width=2,
                   activebackground='powder blue')
    brack2.grid(row=5,column=6)
 
 #calling main loop    
    gui.mainloop()    