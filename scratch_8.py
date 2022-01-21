from tkinter import *
import smtplib
from email.message import EmailMessage
from PIL import Image,ImageTk


server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
def login():
    server.login(e10.get(),e11.get())
    shivam2=Toplevel()
    shivam2.geometry('1640x1680')
    load = Image.open('social-media-bots.jpg')
    render = ImageTk.PhotoImage(load)
    img = Label(shivam2, image=render)
    img.place(x=0,y=0)
    l1=Label(shivam2,text='Your Id:',bg='Cyan',fg='Black')
    l1.place(x=0,y=0)
    e1=Entry(shivam2,bg='Cyan',fg='White')
    e1.place(x=100,y=0)
    l2=Label(shivam2,text='''Send To:''',bg='Cyan',fg='Black')
    l2.place(x=0,y=25)
    e6=Entry(shivam2,bg='Cyan',fg='White')
    e6.place(x=100,y=25)
    #shivam2.mainloop()
    #shivam3=Tk()
    l3=Label(shivam2,text='Subject',bg='Cyan',fg='Black')
    l3.place(x=0,y=50)
    e3=Entry(shivam2,bg='Cyan',fg='White')
    e3.place(x=100,y=50)
    l4=Label(shivam2,text='Body',bg='Cyan',fg='Black')
    l4.place(x=0,y=75)
    e4=Text(shivam2,height=22,width=73,bg='Cyan',fg='White')
    e4.place(x=100,y=75)
    b=Button(shivam2,text='Send Mail',bg='Cyan',fg='Black',command='send_mail')
    b.place(x=630,y=445)
    shivam2.mainloop()
    def send_mail():
        em=EmailMessage()
        em['From']=e1.get()
        em['To']=e6.get()
        em['Subject']=e3.get()
        em.set_content(e4.get())






        server.send_message(em)




shivam1=Tk()
shivam1.geometry('1200x700')
load=Image.open('harsh_email_bot.jpeg')
render=ImageTk.PhotoImage(load)
img=Label(shivam1,image=render)
img.place(x=0,y=0)
l1=Label(shivam1,text='Email',bg='Crimson')
l1.place(x=0,y=0)
e10=Entry(shivam1,bg='Crimson')
e10.place(x=100,y=0)

l2=Label(shivam1,text='Password',bg='Crimson')
l2.place(x=0,y=25)
e11=Entry(shivam1,bg='Crimson',show='*')
e11.place(x=100,y=25)

Button(shivam1,text='Login',command=login,bg='Crimson').place(x=50,y=50)
shivam1.mainloop()