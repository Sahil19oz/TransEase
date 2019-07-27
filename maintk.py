import tkinter as tk
from pymongo import MongoClient
from time import sleep
from datetime import date
#from PIL import ImageTk, Image

connection=MongoClient("localhost",27017)
database=connection["transEase"]
collection1=database["Userdata"]
collection2=database["Transaction"]
global USERID
global PASSWORD
USERID="sahiloz"
PASSWORD="agarwal"
EMAIL="198sahilagarwal@gmail.com"

def format_json(document):
    final_str=""
    for doc in document:
        #try:
            date=doc["date"]
            credit=doc["credit"]
            debit=doc["debit"]
            final_str+='Date:%s  Credit:%s  Debit:%s\n' % (date, credit, debit)
            #res.append(final_str)
            

           #res="There is no entry for the user with Phone:%s"%(document["phone"])
    return final_str
    
    
def page1():
    t1=tk.Toplevel(mainpage)
    canvas2=tk.Canvas(t1,height=HEIGHT,width=WIDTH)
    canvas2.pack()
    background_label=tk.Label(t1,image=background_img)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    f20=tk.Frame(t1,bg="#E0FFFF",bd=5)
    f20.place(rely=0.25,relwidth=1,relheight=0.3)
    b21=tk.Button(f20,text="Make Transaction",font=50,command=maketransaction)
    b21.place(relx=0.4,rely=0.2,relwidth=0.3,relheight=0.2)
    b22=tk.Button(f20,text="Main Menu",font=50,command=menu1)
    b22.place(relx=0.4,rely=0.6,relwidth=0.3,relheight=0.2)

def maketransaction():
    def actual_trans():
        data={
            "phone":e1.get(),
            "date":date.today().strftime("%d/%m/%Y"),
            "debit":int(e12.get()),
            "credit":int(e13.get()),
            "balance":(int(e13.get())-int(e12.get()))
            }
        e1.delete(0,"end")
        e12.delete(0,"end")
        e13.delete(0,"end")
        collection2.insert_one(data)
        sleep(1)
        t4.destroy()
    t4=tk.Toplevel()
    canvas=tk.Canvas(t4,height=HEIGHT,width=WIDTH)
    canvas.pack()
    background_label=tk.Label(t4,image=background_img)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    f1=tk.Frame(t4,bg="#E0FFFF",bd=5)
    f1.place(relx=0.5,rely=.20,relwidth=0.90,relheight=0.5,anchor="n")
    label=tk.Label(f1,text="Phone No:",font=40)
    label.place(relx=0.1,rely=0.1,relwidth=0.3,relheight=0.15)
    e1=tk.Entry(f1)
    e1.place(relx=0.4,rely=0.1,relwidth=0.5,relheight=0.15)
    label1=tk.Label(f1,text="DEBIT:",font=40)
    label1.place(relx=0.1,rely=0.3,relwidth=0.3,relheight=0.15)
    e12=tk.Entry(f1)
    e12.insert(0,"0")
    e12.place(relx=0.4,rely=0.3,relwidth=0.5,relheight=0.15)
    label2=tk.Label(f1,text="CREDIT:",font=40)
    label2.place(relx=0.1,rely=0.5,relwidth=0.3,relheight=0.15)
    e13=tk.Entry(f1)
    e13.insert(0,'0')
    e13.place(relx=0.4,rely=0.5,relwidth=0.5,relheight=0.15)
    button1=tk.Button(f1,text="Make Entry",font=40,command=actual_trans)
    button1.place(relx=.35,rely=.7,relwidth=0.25,relheight=.15)
    
def menu1():
    t2=tk.Tk()
    canvas=tk.Canvas(t2,height=HEIGHT,width=WIDTH)
    canvas.pack()
##    background_img1=tk.PhotoImage(file="landscape.png")
##    background_label=tk.Label(t2,image=background_img1)
##    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    label=tk.Label(t2,text="HELLO ADMIN",font=50)
    label.place(relx=0.4,rely=0.0)
    f1=tk.Frame(t2,bg="#80c1ff",bd=5)
    f1.place(relx=0.5,rely=.10,relwidth=0.90,relheight=0.1,anchor="n")
    button1=tk.Button(f1,text="Search Customer",font=40,command=look_customer)
    button1.place(relx=.00,rely=.1,relwidth=0.25,relheight=.80)
    button2=tk.Button(f1,text="Add Customer",font=40,command=addcus)
    button2.place(relx=.40,rely=.1,relwidth=0.20,relheight=.80)
    button3=tk.Button(f1,text="Delete Customer",font=20)
    button3.place(relx=.75,rely=.1,relwidth=0.25,relheight=0.80)

def look_customer():
    def get_db():
        query={"phone":e11.get()}
        result=collection2.find(query,{"_id":0})
        label["text"]=format_json(result)
    t3=tk.Toplevel()
    canvas=tk.Canvas(t3,height=HEIGHT,width=WIDTH)
    canvas.pack()
    background_label=tk.Label(t3,image=background_img)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    lab11=tk.Label(t3,text="LOOK FOR CUSTOMER RECENT TRANSACTION",font=40)
    lab11.place(relx=0.2,rely=0.03,relwidth=0.6,relheight=0.15)
    f11=tk.Frame(t3)
    f11.place(relx=0.50,rely=.2,relwidth=0.90,relheight=0.1,anchor="n")
    e11=tk.Entry(f11,font=40)
    e11.place(rely=0.2,relwidth=0.60,relheight=1)
    e11.focus()
    
    b11=tk.Button(f11,text="Search",font=40,command=get_db)
    b11.place(relx=.60,rely=0.2,relwidth=0.4,relheight=1)
    t3.bind('<Return>', lambda event=None: b11.invoke())

    f12=tk.Frame(t3,bg="#E0FFFF")
    f12.place(relx=0.50,rely=.35,relwidth=0.8,relheight=0.50,anchor="n")
    label=tk.Label(f12)
    label.place(relwidth=1,relheight=1)

def addcus():
    def user_data():
        name=e11.get()
        phone=e12.get()
        email=e13.get()
        add=e14.get()  
        data={"name":name,
              "phone":phone,
              "email":email,
              "address":add
            }
        e11.delete(0, 'end')
        e12.delete(0, 'end')
        e13.delete(0, 'end')
        e14.delete(0, 'end')
        collection1.insert_one(data)
        sleep(3)
        tp.destroy()
    tp=tk.Toplevel()
    canvas1=tk.Canvas(tp,height=HEIGHT,width=WIDTH)
    canvas1.pack()
    background_label=tk.Label(tp,image=background_img)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    label1=tk.Label(tp,text="ADD NEW CUSTOMER",font=50)
    label1.place(relx=0.4,rely=0.0)
    f11=tk.Frame(tp,bg="#E0FFFF",bd=5)
    f11.place(relx=0.5,rely=.10,relwidth=0.80,relheight=0.8,anchor="n")
    l1=tk.Label(f11,text="NAME:",font=40)
    l1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)
    e11=tk.Entry(f11)
    e11.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.1)
    l2=tk.Label(f11,text="PHONE NO:",font=40)
    l2.place(relx=0.1,rely=0.3,relwidth=0.2,relheight=0.1)
    e12=tk.Entry(f11)
    e12.place(relx=0.3,rely=0.3,relwidth=0.5,relheight=0.1)
    l3=tk.Label(f11,text="Email:",font=40)
    l3.place(relx=0.1,rely=0.5,relwidth=0.2,relheight=0.1)
    e13=tk.Entry(f11)
    e13.place(relx=0.3,rely=0.5,relwidth=0.5,relheight=0.1)
    l4=tk.Label(f11,text="Address:",font=40)
    l4.place(relx=0.1,rely=0.7,relwidth=0.2,relheight=0.1)
    e14=tk.Entry(f11)
    e14.place(relx=0.3,rely=0.7,relwidth=0.5,relheight=0.1)
    b15=tk.Button(f11,text="Submit",font=50,command=user_data)
    b15.place(relx=0.4,rely=0.85)
    tp.mainloop()

def login():
    if (e01.get()==USERID and e02.get()==PASSWORD):
        page1()
    else:
        #tkMessageBox.showinfo( "ERROR", "Invalid Credentials")
        e01.delete(0,"end")
        e02.delete(0,"end")
    
HEIGHT=500
WIDTH=600
mainpage=tk.Tk()



canvas1=tk.Canvas(mainpage,height=HEIGHT,width=WIDTH)
canvas1.pack()
#img = ImageTk.PhotoImage(Image.open("images.jpg"))
#canvas1.create_image(relwidth=1,relheight=1, image=img)
background_img=tk.PhotoImage(file="landscape.png")
background_label=tk.Label(mainpage,image=background_img)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

label01=tk.Label(mainpage,text="Welcome To TransEase",font=60)
label01.place(relx=0.35,rely=0.05)

f011=tk.Frame(mainpage,bg="#E0FFFF")
f011.place(relx=0.5,rely=.20,relwidth=0.60,relheight=0.35,anchor="n")

label001=tk.Label(f011,text="USERID:",font=40)
label001.place(relx=0.1,rely=0.1,relwidth=0.3,relheight=0.20)
e01=tk.Entry(f011,font=40)
e01.place(relx=0.4,rely=0.1,relwidth=0.5,relheight=.20)
e01.focus()

label002=tk.Label(f011,text="PASSWORD:",font=40)
label002.place(relx=0.1,rely=0.3,relwidth=0.3,relheight=0.20)
e02=tk.Entry(f011,show="*",font=40)
e02.place(relx=0.4,rely=0.3,relwidth=0.5,relheight=.20)

b011=tk.Button(f011,text="LOGIN",font=40,command=login)
b011.place(relx=.30,rely=0.5,relwidth=0.4,relheight=.20)
mainpage.bind('<Return>', lambda event=None: b011.invoke())

mainpage.mainloop()
