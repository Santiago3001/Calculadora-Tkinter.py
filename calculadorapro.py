from __future__ import division
from ast import Expression
from distutils.cmd import Command
from tkinter import *
from unicodedata import decimal
#from tkmacosx import Button

ventana = Tk()
ventana.configure(background='#333333')
ventana.title('Calculadora')
ventana.geometry('386x168')

#El entry va a usar 4 columnas de ancho 
equation = StringVar()

def press(num):
    equation.set(equation.get()+ str(num))
    

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('error')
        
def limpiar():
    equation.set('')

expression_entry= Entry(ventana, textvariable=equation)
expression_entry.grid( row=0, columnspan=4, sticky='nswe')

btn7= Button(ventana, text=' 7 ', fg='#fff', background='#666', command=lambda: press(7))
btn7.grid(row=1, column=0, sticky='nswe')

btn8= Button(ventana, text=' 8 ', fg='#fff',background='#666',command=lambda: press(8))
btn8.grid(row=1, column=1, sticky='nswe')

btn9= Button(ventana, text=' 9 ', fg='#fff', background='#666',command=lambda: press(9))
btn9.grid(row=1, column=2, sticky='nswe')

btn4= Button(ventana, text=' 4 ', fg='#fff', background='#666',command=lambda: press(4))
btn4.grid(row=2, column=0, sticky='nswe')

btn5= Button(ventana, text=' 5 ', fg='#fff', background='#666',command=lambda: press(5))
btn5.grid(row=2, column=1, sticky='nswe')

btn6= Button(ventana, text=' 6 ', fg='#fff', background='#666',command=lambda: press(6))
btn6.grid(row=2, column=2, sticky='nswe')

btn0= Button(ventana, text=' 0 ', fg='#fff', background='#666',command=lambda: press(0))
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

btn1= Button(ventana, text=' 1 ', fg='#fff', background='#666',command=lambda: press(1))
btn1.grid(row=3, column=0, sticky='nswe')

btn2= Button(ventana, text=' 2 ', fg='#fff', background='#666',command=lambda: press(2))
btn2.grid(row=3, column=1, sticky='nswe')

btn3= Button(ventana, text=' 3 ', fg='#fff', background='#666',command=lambda: press(3))
btn3.grid(row=3, column=2, sticky='nswe')

decim= Button(ventana, text=' . ', fg='#fff', background='#666',command=lambda: press('.'))
decim.grid(row=4, column=2, sticky='nswe')

suma = Button(ventana, text=' + ', fg='#fff', bg='#fe9727',command=lambda: press('+'))
suma.grid(row=1, column=3, sticky='nswe')

resta = Button(ventana, text=' - ', fg='#fff', bg='#fe9727',command=lambda: press('-'))
resta.grid(row=2, column=3, sticky='nswe')

multiplicacion = Button(ventana, text=' * ', fg='#fff', bg='#fe9727',command=lambda: press('*'))
multiplicacion.grid(row=3, column=3, sticky='nswe')

division = Button(ventana, text=' / ', fg='#fff', bg='#fe9727',command=lambda: press('/'))
division.grid(row=4, column=3, sticky='nswe')

igual= Button(ventana, text=' = ',fg='#fff', bg='#fe9727', command= equalpress)
igual.grid(row=5, column=3, sticky='nswe')

clear= Button(ventana, text=' clear ',fg='#fff', bg='#999', command=limpiar)
clear.grid(row=5, column=2, sticky='nswe')



ventana.mainloop()
