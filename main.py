from tkinter import *
import  datetime
import sqlite3
from tkinter import  messagebox

date=datetime.datetime.now()
date=date.strftime('%d-%m-%y')

conn=sqlite3.connect('phonebook.db')
cur=conn.cursor()
class Phonebook(object):
    def __init__(self,master):
        self.master=master
        top=Frame(master,height=150,bg='blue',bd=8,relief=GROOVE)
        top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='skyblue', bd=8, relief=GROOVE)
        self.bottom.pack(fill=X)
        heading=Label(top,text='My PhoneBook App',font='arial 40 bold',bg='blue',fg='orange')
        heading.place(x=60,y=30)
        date1 = Label(top, text="Today's date: "+date, font='arial 15 bold', bg='blue')
        date1.place(x=370, y=100)
        self.signup_design()

    def signup_design(self):
        f1=Frame(self.bottom,height=340,width=390,bg='pink',bd=15,relief=GROOVE)
        f1.place(x=120,y=40)
        f2 = Frame(f1, height=300, width=350, bd=8, relief=GROOVE)
        f2.place(x=6, y=6)
        Label(f2,text='SignUp page',font='arial 25 bold',fg='blue').place(x=80,y=10)
        Label(f2,text='User Name',font='arial 18 bold').place(x=10,y=90)
        self.name_e=Entry(f2,bd=3)
        self.name_e.place(x=160,y=95,height=28,width=170)
        Label(f2, text='Password', font='arial 18 bold').place(x=10, y=150)
        self.pwd_e = Entry(f2, bd=3)
        self.pwd_e.place(x=160, y=155, height=28, width=170)

        btn1=Button(f2,width=7,text='SignUp',font='arial 15 bold',bd=4,relief=GROOVE,bg='pink',command=self.signup)
        btn1.place(x=130,y=210)

        btn2 = Button(f2,height=2, width=13, text='Login', font='arial 7 bold', bd=4, relief=GROOVE, bg='green',command=self.login_design)
        btn2.place(x=5, y=240)

    def signup(self):
        n = self.name_e.get()
        p = self.pwd_e.get()

        if n and p !='':
            cur.execute('CREATE TABLE IF NOT EXISTS login(name TEXT,password TEXT)')
            cur.execute('INSERT INTO login(name,password)VALUES(?,?)',(n,p))
            conn.commit()
            messagebox.showinfo('Success', 'SignUp Successfull')
        else:
            messagebox.showinfo('Information', 'Enter user name and password')
    def login_design(self):
        f1=Frame(self.bottom,height=340,width=390,bg='pink',bd=15,relief=GROOVE)
        f1.place(x=120,y=40)
        f2 = Frame(f1, height=300, width=350, bd=8, relief=GROOVE)
        f2.place(x=6, y=6)
        Label(f2,text='Login page',font='arial 25 bold',fg='blue').place(x=80,y=10)
        Label(f2,text='User Name',font='arial 18 bold').place(x=10,y=90)
        self.name_e=Entry(f2,bd=3)
        self.name_e.place(x=160,y=95,height=28,width=170)
        Label(f2, text='Password', font='arial 18 bold').place(x=10, y=150)
        self.pwd_e = Entry(f2, bd=3)
        self.pwd_e.place(x=160, y=155, height=28, width=170)

        btn1=Button(f2,width=7,text='Login',font='arial 15 bold',bd=4,relief=GROOVE,bg='pink',command=self.login)
        btn1.place(x=130,y=210)

        btn2 = Button(f2,height=2, width=13, text='Change password', font='arial 7 bold', bd=4, relief=GROOVE, bg='green',command=self.Change_design)
        btn2.place(x=5, y=240)

    def login(self):
        n=self.name_e.get()
        p=self.pwd_e.get()
        result=cur.execute("select * from login").fetchall()

        for i in result:
            name=i[0]
            pwd=i[1]
            if n!=''or p!='':
                if name==n and pwd==p:
                    x=name
                    y=pwd

        if n != '' or p != '':
            if x == n and y == p:
                login = Main_page()
                messagebox.showinfo('Success', 'Login Successfull')
            else:
                messagebox.showerror('Error', 'Invalid user name and password')
        else:
            messagebox.showinfo('Information', 'Enter user name and password')
    def Change_design(self):
        f1=Frame(self.bottom,height=340,width=390,bg='pink',bd=15,relief=GROOVE)
        f1.place(x=120,y=40)
        f2 = Frame(f1, height=300, width=350, bd=8, relief=GROOVE)
        f2.place(x=6, y=6)
        Label(f2,text='Change Password',font='arial 20 bold',fg='blue').place(x=50,y=10)

        Label(f2,text='User Name',font='arial 15 bold').place(x=10,y=70)
        self.name_e=Entry(f2,bd=3)
        self.name_e.place(x=180,y=75,height=28,width=150)

        Label(f2, text='Old password', font='arial 15 bold').place(x=10, y=110)
        self.oldpwd_e = Entry(f2, bd=3)
        self.oldpwd_e.place(x=180, y=115, height=28, width=150)

        Label(f2, text='New password', font='arial 15 bold').place(x=10, y=150)
        self.newpwd_e = Entry(f2, bd=3)
        self.newpwd_e.place(x=180, y=155, height=28, width=150)


        btn1=Button(f2,width=7,text='Change',font='arial 15 bold',bd=4,relief=GROOVE,bg='pink',command=self.change_password)
        btn1.place(x=130,y=210)

        btn2 = Button(f2,height=2, width=13, text='login', font='arial 7 bold', bd=4, relief=GROOVE, bg='green',command=self.login_design)
        btn2.place(x=5, y=240)

    def change_password(self):
        n=self.name_e.get()
        o_p=self.oldpwd_e.get()
        n_p=self.newpwd_e.get()

        result = cur.execute("select * from login").fetchall()
        for i in result:
            name = i[0]
            pwd = i[1]
            if n != '' or o_p != '' or n_p:
                if name == n and pwd == o_p:
                    x=name
                    y=pwd

        if n != '' or o_p != '' or n_p!='':
            if x == n and y == o_p:
                cur.execute("Update login set password=? where name=? and password=?",(n_p,n,o_p))
                conn.commit()
                messagebox.showinfo('Success','Password changed')
            else:
                messagebox.showerror('Error', 'Invalid user name and old password')
        else:
            messagebox.showinfo('Information', 'Fill all field')
class Main_page(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('My people')
        self.geometry('1000x690+170+10')
        self.resizable(False,False)

        top = Frame(self, height=200, bg='blue', bd=8, relief=GROOVE)
        top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='skyblue', bd=8, relief=GROOVE)
        self.bottom.pack(fill=X)
        heading = Label(top, text='My PhoneBook App', font='arial 55 bold', bg='blue', fg='orange')
        heading.place(x=70, y=10)
        date1 = Label(top, text="Today's date: " + date, font='arial 18 bold', bg='blue')
        date1.place(x=670, y=95)

        f1=Frame(self.bottom,height=325,width=220,bg='blue',bd=5,relief=GROOVE)
        f1.place(x=60,y=70)
        f2 = Frame(f1, height=295, width=190, bd=5, relief=GROOVE)
        f2.place(x=10, y=10)

        btn1=Button(f2,text='My People',width=9,font='arial 18 bold',bd=5,bg='skyblue',relief=GROOVE,command=self.my_people)
        btn1.place(x=10,y=30)
        btn2 = Button(f2, text='Add People',width=9, font='arial 18 bold', bd=5, bg='white', relief=GROOVE,command=self.add_people)
        btn2.place(x=10, y=110)
        btn3 = Button(f2, text='AboutUs',width=9, font='arial 18 bold', bd=5, bg='pink', relief=GROOVE,command=self.about_us)
        btn3.place(x=10, y=190)

    def add_people(self):
        self.f1=Frame(self.bottom,height=460,width=600,bd=10,relief=GROOVE,bg='white')
        self.f1.place(x=370,y=10)
        Label(self.f1,text='Add people form',font='arial 25 bold',bg='white',fg='blue').place(x=150,y=10)

        fname=Label(self.f1,text='First Name',font='arial 15 bold',bg='white')
        fname.place(x=80,y=100)
        self.fname_e=Entry(self.f1,bd=3)
        self.fname_e.place(x=220,y=100,height=30,width=290)

        lname = Label(self.f1, text='Last Name', font='arial 15 bold', bg='white')
        lname.place(x=80, y=150)
        self.lname_e = Entry(self.f1, bd=3)
        self.lname_e.place(x=220, y=150, height=30, width=290)

        email = Label(self.f1, text='Email', font='arial 15 bold', bg='white')
        email.place(x=80, y=210)
        self.email_e = Entry(self.f1, bd=3)
        self.email_e.place(x=220, y=210, height=30, width=290)

        mob = Label(self.f1, text='Moblie no', font='arial 15 bold', bg='white')
        mob.place(x=80, y=270)
        self.mob_e = Entry(self.f1, bd=3)
        self.mob_e.place(x=220, y=270, height=30, width=290)

        address = Label(self.f1, text='Address', font='arial 15 bold', bg='white')
        address.place(x=80, y=330)
        self.address_e = Text(self.f1, bd=5)
        self.address_e.place(x=220, y=320, height=60, width=290)

        btn=Button(self.f1,width=7,text='Add',bd=5,font='arial 13 bold',bg='skyblue',command=self.add_record)
        btn.place(x=250,y=390)

    def add_record(self):
        fname=self.fname_e.get()
        lname=self.lname_e.get()
        email=self.email_e.get()
        mob=self.mob_e.get()
        address=self.address_e.get(1.0,'end-1c')
        #print(fname,lname,email,mob,address)

        if fname and lname and email and mob and address !='':
            cur.execute('CREATE TABLE IF NOT EXISTS addpeople(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL\
                        ,FNAME TEXT,LNAME TEXT,EMAIL TEXT,MOBILE INTEGER,ADDRESS TEXT)')
            cur.execute('INSERT INTO addpeople(FNAME,LNAME,EMAIL,MOBILE,ADDRESS)VALUES(?,?,?,?,?)',
                        (fname,lname,email,mob,address))
            conn.commit()
            msg1=Label(self.f1,text="Record added successfully",font='arial 12 bold',bg='white',fg='green')
            msg1.place(x=80,y=60)
        else:
            msg2 = Label(self.f1, text="Fill details of person", font='arial 12 bold', bg='white', fg='red')
            msg2.place(x=80, y=60)

    def my_people(self):
        f1=Frame(self.bottom,height=450,width=600)
        f1.place(x=370,y=10)
        f2 = Frame(f1, height=70, width=600,bg='pink',bd=10,relief=GROOVE)
        f2.place(x=0, y=0)
        f3= Frame(f1, height=400, width=600, bg='pink', bd=10, relief=GROOVE)
        f3.place(x=0, y=60)

        heading=Label(f2,text='My People Page',font='arial 25 bold',bg='pink')
        heading.place(x=150,y=5)

        scroll=Scrollbar(f3,orient=VERTICAL)
        self.listbox=Listbox(f3,width=58,height=23)
        self.listbox.grid(row=0,column=0,padx=(40,0))
        scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scroll.set)
        scroll.grid(row=0,column=1,sticky=NS)

        person=cur.execute("SELECT * FROM addpeople").fetchall()
        self.listbox.insert(END,"S.NO   NAME")
        self.listbox.insert(END,"------------------------------------------")

        for i in person:
            self.listbox.insert(END,str(i[0])+".        "+i[1]+" "+i[2])




        btnadd=Button(f3,text='Add',width=12,font='Sans 12 bold',command=self.add_people)
        btnadd.grid(row=0,column=2,padx=20,pady=10,sticky=N)
        btndisplay = Button(f3, text='Display', width=12, font='Sans 12 bold',command=self.display_selectid)
        btndisplay.grid(row=0, column=2, padx=20, pady=50, sticky=N)
        btnupdate = Button(f3, text='Update', width=12, font='Sans 12 bold',command=self.update_selectid)
        btnupdate.grid(row=0, column=2, padx=20, pady=90, sticky=N)
        btndelete = Button(f3, text='Delete', width=12, font='Sans 12 bold',command=self.delete_record)
        btndelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    def display_selectid(self):
        try:
            selected_item =self.listbox.curselection()
            person =self.listbox.get(selected_item)
            self.person =person.split(".")[0]
            self.display()
        except:
            pass
    def display(self):
        r=Tk()
        r.title('Display people')
        r.geometry('410x460+550+200')
        r.resizable(False,False)

        try:
            query="select * from addpeople where ID='{}'".format(self.person)
            result=cur.execute(query).fetchone()
            fn=result[1]
            ln=result[2]
            e=result[3]
            m=result[4]
            a=result[5]
        except:
            pass
        top =Frame(r,height=60,bg='skyblue')
        top.pack(fill=X)
        bottom = Frame(r, height=500, bg='lightgray')
        bottom.pack(fill=X)

        Label(top,text='Display people',font='arial 20 bold',bg='skyblue',fg='blue').place(x=100,y=15)

        fname=Label(bottom, text='First name', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=30)
        lname = Label(bottom, text='Last name', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=70)
        email = Label(bottom, text='Email', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=110)
        mob = Label(bottom, text='Mobile no', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=150)
        address = Label(bottom, text='Address', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=190)

        d_fname = Label(bottom,text=fn, font='arial 10 bold', bg='lightgray').place(x=180, y=35)
        d_lname = Label(bottom,text=ln, font='arial 10 bold', bg='lightgray').place(x=180, y=75)
        d_email = Label(bottom,text=e, font='arial 10 bold', bg='lightgray').place(x=180, y=115)
        d_mob = Label(bottom,text=m, font='arial 10 bold', bg='lightgray').place(x=180, y=155)
        d_address = Label(bottom,text=a, font='arial 10 bold', bg='lightgray').place(x=180, y=195)


    def update_selectid(self):
        try:
            selected_item =self.listbox.curselection()
            person =self.listbox.get(selected_item)
            self.person =person.split(".")[0]
            self.update()
        except:
            pass
    def update(self):
        r2=Tk()
        r2.title('Update people')
        r2.geometry('410x460+550+200')
        r2.resizable(False,False)

        try:
            query="select * from addpeople where ID='{}'".format(self.person)
            result=cur.execute(query).fetchone()
            fn=result[1]
            ln=result[2]
            e=result[3]
            m=result[4]
            a=result[5]
        except:
            pass
        top =Frame(r2,height=60,bg='skyblue')
        top.pack(fill=X)
        self.btm = Frame(r2, height=500, bg='lightgray')
        self.btm .pack(fill=X)

        Label(top,text='Update people',font='arial 20 bold',bg='skyblue',fg='blue').place(x=100,y=15)

        fname=Label(self.btm , text='First name', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=30)
        lname = Label(self.btm , text='Last name', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=70)
        email = Label(self.btm , text='Email', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=110)
        mob = Label(self.btm , text='Mobile no', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=150)
        address = Label(self.btm , text='Address', font='arial 15 bold', bg='lightgray', fg='blue').place(x=40, y=190)

        self.e_fn=Entry(self.btm ,width=35,bd=3)
        self.e_fn.insert(1,fn)
        self.e_fn.place(x=160,y=30)

        self.e_ln = Entry(self.btm , width=35, bd=3)
        self.e_ln.insert(1, ln)
        self.e_ln.place(x=160, y=70)

        self.e_e = Entry(self.btm , width=35, bd=3)
        self.e_e.insert(1, e)
        self.e_e.place(x=160, y=110)

        self.e_m = Entry(self.btm , width=35, bd=3)
        self.e_m.insert(1, m)
        self.e_m.place(x=160, y=150)

        self.e_a = Entry(self.btm , width=35, bd=3)
        self.e_a.insert(1, a)
        self.e_a.place(x=160, y=190)

        btn=Button(self.btm ,width=9,text='UPDATE',bd=5,bg='skyblue',command=self.update_record)
        btn.place(x=180,y=260)

    def update_record(self):
        id=self.person
        fname=self.e_fn.get()
        lname=self.e_ln.get()
        email=self.e_e.get()
        mobile=self.e_m.get()
        address=self.e_a.get()

        query="update addpeople set FNAME='{}',LNAME='{}',EMAIL='{}',MOBILE='{}',ADDRESS='{}'\
               where id={}".format(fname,lname,email,mobile,address,id)
        cur.execute(query)
        conn.commit()
        msg=Label(self.btm,text='Updated successfully',font='arial 12 bold',bg='lightgray',fg='green')
        msg.place(x=40,y=5)

    def delete_record(self):
        try:
            selected_item = self.listbox.curselection()
            person = self.listbox.get(selected_item)
            person = person.split(".")[0]
            query="delete from addpeople where id={}".format(person)
            cur.execute(query)
            conn.commit()
        except:
            pass

    def about_us(self):
        f1=Frame(self.bottom,height=460,width=600,bd=10,relief=GROOVE,bg='skyblue')
        f1.place(x=370,y=10)
        Label(f1,text='About Us Page\n********************************************',font='arial 25 bold',bg='skyblue',fg='blue').place(x=0,y=15)
        lb1=Label(f1,text='We simplify your life by allowing'
                          '\n you to effortlessly add, view, and delete contacts,\n all within a sleek and intuitive interface.'
                          '\n Our mission is to keep you connected seamlessly \nwhile ensuring your data is secure and accessible.'
                          '\n  Join our community and experience the future of \ncontact management today!'
                  ,font='arial 15 bold',bg='skyblue')
        lb1.place(x=15,y=90)
def main():
    win=Tk()
    app=Phonebook(win)
    win.title('Myphonebookapp')
    win.geometry('650x570+500+80')
    win.resizable(False,False)
    win.mainloop()
main()