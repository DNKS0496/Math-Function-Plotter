# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:25:38 2020

@author: p
"""

import matplotlib.pyplot as plt
import math
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter import messagebox
else:
    import tkinter as tk
    from tkinter import messagebox

#Create Window
    
window = tk.Tk()
window.title("Math Plot")
window.geometry("240x300")
window.resizable(0,0)

#Create Frames for grouping
frame1 = tk.Frame(window)
frame1.pack()
frame1.configure(bg='#606060', border=2, highlightbackground='#000000', highlightthickness=2)

frame2 = tk.Frame(window)
frame2.pack(padx=5)
frame2.configure(bg='#FFB266', border=10, highlightbackground='#000000', highlightthickness=2)

#Give labels to the respective frames

lbl = tk.Label(frame1, text="Math Function Plotter", font=("bold", 15), bg='#606060', fg='#FFFFFF')
lbl.pack( side = 'top', padx=10, pady=5)

lbl2 = tk.Label(frame2, text="Please enter an integer value <=700", bg='#FFB266')
lbl2.grid(row=0, column=0, columnspan=20)

#Create text box for input from user

txt = tk.Entry(frame2, width=30, highlightbackground='#000000', highlightthickness=1)
txt.grid(row=1, column=0, columnspan=20, pady=5)
txt.focus()

#Function for validating and generating x-values for all functions except own function

def x_val():
    '''Function to check input value and generate x for calculating y'''
    try:
        x = int(txt.get())
        if x<=700 and x>=0:
            return [i for i in range(x)]
        else:
            raise Exception
    except Exception:
        messagebox.showinfo("Error", "Please enter a positive integer in range 0 to 700 both inclusive")
        return None
        
def plot(x, y):
    plt.xlabel("X-value in given range")
    plt.ylabel("Y-value in given range")
    plt.title("Function Plots")
    plt.plot(x,y, label='Graph')
    plt.show()
    
#Defining functions for buttons

def cos():
    x = x_val()
    if x is not None:
      y = [math.cos(math.radians(j)) for j in x]
      plot(x,y)      

    
def sin():
    x = x_val()
    if x is not None:
      y = [math.sin(math.radians(j)) for j in x]
      plot(x,y)   
    
def tan():
    x = x_val()
    if x is not None:
      y = [math.tan(math.radians(j)) for j in x]
      plot(x,y)   
    
def exp():
    x = x_val()
    if x is not None:
      y = [math.exp(j) for j in x]
      plot(x,y)   
    
def sqrt():
    if x_val() is not None:
        x = [val for val in x_val() if val>0]
        y = [math.sqrt(j) for j in x]
        plot(x,y)   
    
def log():
    if x_val() is not None:
        x = [val for val in x_val() if val>0]
        y = [math.log(j) for j in x]
        plot(x,y)   
    
def erf():
    x = x_val()
    if x is not None:
      y = [math.erf(j) for j in x]
      plot(x,y)   
      
def own():
    dic = {'log':math.log, 'e':math.exp, 'sqrt':math.sqrt}
    y=[]
    expr = txt.get()
    try:
        if 'x' not in expr:
            raise Exception
            
        for x in range(1,401):
            dic['x'] = x
            y.append(eval(expr, {'__builtins__()':None}, dic))
        x = range(1,401)
        plot(x,y)
    except Exception:
         messagebox.showinfo("Error", "Please enter a valid expression in lower case 'x' containing:\n1. x\n2. log(x)\n3. e(x)\n4. sqrt(x)\n5. x**n (n is any integer)")
        
def exit1():
    window.destroy()
    
def clear():
    plt.close()
    txt.delete(0, 'end')
    
#Creating Buttons

btn = tk.Button(frame2, text="cos(deg)", width=7, height=2, command=cos)
btn.grid(row=2, column=0, padx=2, pady=2)

btn = tk.Button(frame2, text="sin(deg)", width=7, height=2, command=sin)
btn.grid(row=2, column=1, padx=2, pady=2)
    
btn = tk.Button(frame2, text="tan(deg)", width=7, height=2, command=tan)
btn.grid(row=2, column=2, padx=2, pady=2)
    
btn = tk.Button(frame2, text="exp", width=7, height=2, command=exp)
btn.grid(row=3, column=0, padx=2, pady=2)
    
btn = tk.Button(frame2, text="sqrt", width=7, height=2, command=sqrt)
btn.grid(row=3, column=1, padx=2, pady=2)
    
btn = tk.Button(frame2, text="log", width=7, height=2, command=log)
btn.grid(row=3, column=2, padx=2, pady=2)
    
btn = tk.Button(frame2, text="erf", width=7, height=2, command=erf)
btn.grid(row=4, column=0, padx=2, pady=2)

btn = tk.Button(frame2, text="f(x)", width=7, height=2, command=own)
btn.grid(row=4, column=1, padx=2, pady=2)

btn = tk.Button(frame2, text="clear", width=7, height=2, command=clear)
btn.grid(row=4, column=2, columnspan=2, padx=2, pady=2)

btn = tk.Button(frame2, text="exit", width=26, height=2, command=exit1)
btn.grid(row=5, column=0, columnspan=3, pady=5, padx=2)
        
#main function for tkinter GUI
window.mainloop()
