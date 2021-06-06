'''Python Program - Password Generator by DJ Harshit'''

# Importing the modules
from tkinter import *
from passwd import Password

# Colors
brwn = '#c88141'
grn = '#52d017'
bg_brwn = '#7f5217'
bl = '#6698ff'
ch = ''

wind = Tk()

# It gives a random number from list
def give():
    global ch
    pwd=Password(ch, int(e1.get()))
    pwd.setchar()
    pwd.pwdgen()
    p.set(pwd.getpwd())
    ch = ''
    
def gen():
    #Giving password to user
    global ch
    if u.get():
        ch += 'u'
    if l.get():
        ch += 'l'
    if d.get():
        ch += 'd'
    if s.get():
        ch += 's'
    give()

# Initialise int variables
u = IntVar()
d = IntVar()
s = IntVar()
l = IntVar()
p=StringVar()

# Main program
wind.title('Paasword Generator')	
wind.geometry('500x400')
wind.resizable(0,0)
wind.config(bg=brwn)

l1 = Label(wind, text='Password Generator', font=('Bodoni MT', 30, 'bold'), fg=grn,bg=bg_brwn)
l1.grid(row=0, column=0, columnspan=2, pady=10)

l2 = Label(wind, text='By Harshit', font=('Arial', 15, 'bold'), fg=grn, bg=bg_brwn, padx=10, pady=10)
l2.grid(row=0, column=2)

l2 = Label(wind, text='Enter length', font=('Arial', 20, 'bold'), bg=brwn)
l2.grid(row=1, column=0)

e1 = Entry(wind, font=('Arial', 20, 'bold'))
e1.grid(row=1, column=1, columnspan=2)

c1=Checkbutton(wind, text='Uppercase', font=('',15), bg=brwn, variable=u)
c1.grid(row=2, column=0)

c2=Checkbutton(wind, text='Lowercase', font=('',15), bg=brwn, variable=l)
c2.grid(row=2, column=1)

c3=Checkbutton(wind, text='Digits', font=('',15), bg=brwn, variable=d)
c3.grid(row=3, column=0)

c4=Checkbutton(wind, text='Symbols', font=('',15), bg=brwn, variable=s)
c4.grid(row=3, column=1)

b1 = Button(wind, text='Generate', font=('Arial Black', 10), bg='grey', command=gen)
b1.grid(row=4, column=1, pady=10)

l2 = Label(wind, text=' Pwd :', font=('Arial', 20, 'bold'), bg=brwn)
l2.grid(row=5, column=0)

e2 = Entry(wind, font=('Arial', 20, 'bold'), textvariable=p)
e2.grid(row=5, column=1, columnspan=2)

wind.mainloop()
