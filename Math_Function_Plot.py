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

#Functions for different inputs

def x_val():
    '''Function to check input value and generate x for calculating y'''
    try:
        x = int(txt.get())
        if x<=700:
            return [i for i in range(x)]
        else:
            return None
    except:
        messagebox.showinfo("Error", "Please enter a valid integer")
        return None
        
def plot(x, y):
    plt.xlabel("X-value in given range")
    plt.ylabel("Y-value in given range")
    plt.title("Function Plots")
    plt.plot(x,y, label='Graph')
    plt.show()
    

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
    
def log2():
    if x_val() is not None:
        x = [val for val in x_val() if val>0]
        y = [math.log2(j) for j in x]
        plot(x,y)   
    
def erf():
    x = x_val()
    if x is not None:
      y = [math.erf(j) for j in x]
      plot(x,y)   

def exit1():
    window.destroy()

def clear():
    plt.close()
    txt.delete(0, 'end')

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
    
btn = tk.Button(frame2, text="log2", width=7, height=2, command=log2)
btn.grid(row=3, column=2, padx=2, pady=2)
    
btn = tk.Button(frame2, text="erf", width=7, height=2, command=erf)
btn.grid(row=4, column=0, padx=2, pady=2)

btn = tk.Button(frame2, text="clear", width=16, height=2, command=clear)
btn.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

btn = tk.Button(frame2, text="exit", width=26, height=2, command=exit1)
btn.grid(row=5, column=0, columnspan=3, pady=5, padx=2)
        

window.mainloop()
