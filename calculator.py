from tkinter import *
root = Tk()
root.title("Saeed's calculator")
import math
def sin():
    C=float(e3.get())
    print (math.sin((math.radians(C))))
def cos():
    C=float(e3.get())
    print (math.cos((math.radians(C))))
def tan():
    C=float(e3.get())
    print (math.tan((math.radians(C))))
def cot():
    C=float(e3.get())
    print ((math.cos((math.radians(C))))/(math.sin((math.radians(C)))))
def log():
    C=float(e3.get())
    print (math.log(C,10))
def radikal():
    C=float(e3.get())
    print(math.sqrt(C))
def pow():
    C=float(e3.get())
    print(math.pow(C,2))
def radians():
    C=float(e3.get())
    print(math.radians(C))
def factorial():
    C=int(e3.get())
    print(math.factorial(C))
def add():
    A=float(e1.get())
    B=float(e2.get())
    C=A+B
    print(C)
def mul():
    A=float(e1.get())
    B=float(e2.get())
    C=A*B
    print(C)
def tagsim():
     A=float(e1.get())
     B=float(e2.get())
     C=A/B
     print(C)
def menha():
      A=float(e1.get())
      B=float(e2.get())
      C=A-B
      print(C)

Label(root, text="sin&cos$tan&cot&factorial&log&tavan&radians").grid(row=6, column=0)
Label(root, text="first number").grid(row=1, column=0)
Label(root, text='second number').grid(row=2, column=0)
Label(root, text="⇊⇊بخش پیشرفته ماشین حساب⇊⇊").grid(row=3, column=2)

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=6, column=1)
Button(root, text='quit',command=root.quit,fg="red").grid(row=7, column=2)


Button(root, text='+', command=add).grid(row=0, column=1)
Button(root, text='*', command=mul).grid(row=0, column=2)
Button(root, text='/', command=tagsim).grid(row=0, column=3)
Button(root, text=' -', command=menha).grid(row=0, column=4)
Button(root, text='sin', command=sin).grid(row=5, column=1)
Button(root, text='cos', command=cos).grid(row=5, column=2)
Button(root, text='tan', command=tan).grid(row=5, column=3)
Button(root, text='cot', command=cot).grid(row=5, column=8)
Button(root, text='log', command=log).grid(row=5, column=9)
Button(root, text=' be tavan 2', command=pow).grid(row=5, column=11)
Button(root, text=' radians', command=radians).grid(row=5, column=12)
Button(root, text='factorial', command=factorial).grid(row=5, column=13)

























root.mainloop()
