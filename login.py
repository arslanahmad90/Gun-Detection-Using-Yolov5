from tkinter import *
from tkinter import messagebox
import os
import subprocess

root=Tk()
root.title('Login Page')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    with open('datasheet.txt') as f:
        data = f.read()
        credentials = eval(data)
        usernames = list(credentials.keys())
        passwords = list(credentials.values())

    if username in usernames and password in passwords:
        print('Login as Admin in Gun Detection Application ')
        # screen=Toplevel(root)
        # screen.title("Gun Detection Application")
        # screen.geometry('925x500+300+200')
        # screen.config(bg="white")
        root.destroy()
        script="python TkinerGUI.py"
        print("script",script)
        subprocess.call(script, shell=True)
        #Label(screen,text='Hello Iam Here ',bg='#fff',font=('calibry(Body)',50,'bold')).pack(expand=True)
        
        #screen.mainloop()
    elif username !='admin' and password !='1234':
        messagebox.showerror("Invalid","invalid username and password")  

    elif password !='1234':
        messagebox.showerror("Invalid","invalid password") 

    elif username !='admin':
         messagebox.showerror("Invalid","invalid username for Admin")  

img = PhotoImage(file = 'login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
########-------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#################-------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'password')
def signup():
    root.destroy()
    script="python signup.py"
    print("script",script)
    subprocess.call(script, shell=True)


code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave) 
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

####################-----------------

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup).place(x=215,y=270)
#sign_up.

root.mainloop()