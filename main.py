#ADVANCE PASSWORD MANAGER WITH SEARCH OPTION


import json
from tkinter import *
from tkinter import messagebox
import random as r
import pyperclip



#-----------------------------SEARCH BUTTON--------------------------------------#
def search():
    # =e1.get()
    try:
        with open(r"C:\Users\linge\Desktop\python 100 days\projects\pr-30\passdata.json","r") as f:
            r=json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning!!!",message="NO DATA FILE FOUND")
    else:
        for i in r:
            if i==e1.get():
                messagebox.showinfo(title=e1.get(),message=f"E-mail:{r[i]['email']}\nPassword:{r[i]['password']}")
            else:
                messagebox.showerror(title="NOT FOUND!",message=f"NO DETAILS FOR {e1.get()} EXITS")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    al=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    num=['1','2','3','4','5','6','7','8','9','0']
    sy=[ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    nr_letters=r.randint(8,10)
    nr_sys=r.randint(2,4)
    nr_num=r.randint(2,4)

    lett=[r.choice(al) for i in range(nr_letters)]

    number=[r.choice(num) for i in range(nr_num)]

    sys=[r.choice(sy) for i in range(nr_sys)]
    passw=lett+sys+number
    r.shuffle(passw)

    passwords="".join(passw)
    
    e3.insert(0,passwords)
    pyperclip.copy(passwords)
# print(password)yQ=V>IQ'q7jrx1Y8  5VQ+,vC0PZ8d7@T

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data():
    newdata={
        e1.get():{
            "email":e2.get(),
            "password":e3.get()
        }
    }
    if len(e1.get())==0 or len(e2.get())==0:
        messagebox.showinfo(title="Opps!!!!!!!",message="Heyy!! Don't leave any of the feild empty")
    else:
        try:
            with open("passdata.json","r") as f:
                data=json.load(f)
        except FileNotFoundError:
            with open("passdata.json","w") as f:
                json.dump(newdata,f,indent=4)
        else:
            data.update(newdata)
        
            with open("passdata.json","w") as f:
                json.dump(data,f,indent=4)
        finally:
            e1.delete(0,END)
            e2.delete(0,END)
            e2.insert(0,"lingesh.91918@gmail.com")
            e3.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.title("Password Manager🔒")
win.config(padx=50,pady=50,bg="white")
win.minsize(300,300)

canva=Canvas(width=200,height=200,bg="white",highlightthickness=0)
img=PhotoImage(file="logo.png")
canva.create_image(100,100,image=img)
canva.grid(column=1,row=0)

la1=Label(text="Website:",font=('courier',10,"bold"),bg="white")
la1.grid(column=0,row=1)

e1=Entry(width=21)
e1.grid(row=1,column=1)
e1.focus()

la2=Label(text="Email/Username:",font=('courier',10,"bold"),bg="white")
la2.grid(column=0,row=2)

e2=Entry(width=35)
e2.insert(0,"lingesh.91918@gmail.com")
e2.grid(row=2,column=1,columnspan=2)

la3=Label(text="Password🔑:",font=('courier',10,'bold'),bg='white')
la3.grid(row=3,column=0)

e3=Entry(width=21)
e3.grid(row=3,column=1)

but1=Button(text="Generate Password",font=('courier',10,"bold"),bg="white",command=password)
but1.grid(row=3,column=2)



but2=Button(text="ADD",width=36,font=('courier',10,"bold"),bg="white",command=data)
but2.grid(row=4,column=1,columnspan=2)

search=Button(text="Search",width=13,font=('courier',10,"bold"),bg="white",command=search,highlightthickness=0)
search.grid(row=1,column=2)


win.mainloop()
