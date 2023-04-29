from tkinter import *
from tkinter import messagebox
import ast
import subprocess
window=Tk()
window.title("SignUp Page")
window.geometry('925x500+300+200')
window.configure(bg ='#fff')
window.resizable(False,False)

def signup():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()

    if password == confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))
            file.close()
            messagebox.showinfo('signup','sucessfully signup')
            window.destroy()
            script="python login.py"
            print("script",script)
            subprocess.call(script, shell=True)

        except:
            file=open('datasheet.txt','w')
            pp=str({'username':'password'})
            file.write(pp)
            file.close()
            window.destroy()
            script="python login.py"
            print("script",script)
            subprocess.call(script, shell=True)


    else:            
        messagebox.showerror('Invalid',"Both Password should match")


img=PhotoImage(file='signup.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)


frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##############--------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'username')

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##############-----------------------------

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
        code.insert(0,'password')

code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

###################----------------------
def on_enter(e):
    confirm_code.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        confirm_code.insert(0,'confirm password')
def signin():
    window.destroy()
    script="python login.py"
    print("script",script)
    subprocess.call(script, shell=True)
confirm_code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0,'confirm password')
confirm_code.bind('<FocusIn>',on_enter)
confirm_code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

###########################-------------------------------

Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=340)

sign_up=Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin).place(x=215,y=340)
#sign_up.place(x=215,y=340)



window.mainloop()