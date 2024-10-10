import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

class hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, bg=self.clr(220,180,190), text="Hospital Management System",bd=3,relief="groove", font=("Arial",50,"bold"))
        title.pack(side="top", fill="x")

        # input frame

        inFrame = tk.Frame(self.root, bd=4, relief="groove", bg=self.clr(190,180,220))
        inFrame.place(width=self.width/3, height=self.height-180,x=30, y=100 )

        idLbl = tk.Label(inFrame,text="Enter ID:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        idLbl.grid(row=0,column=0, padx=20,pady=15)
        self.idIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.idIn.grid(row=0,column=1,padx=10, pady=15)

        nameLbl = tk.Label(inFrame,text="Enter Name:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        nameLbl.grid(row=1, column=0, padx=20, pady=15)
        self.nameIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.nameIn.grid(row=1, column=1, padx=10, pady=15)

        bgLbl = tk.Label(inFrame,text="B_Group:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        bgLbl.grid(row=2, column=0, padx=20, pady=15)
        self.bgIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.bgIn.grid(row=2, column=1, padx=10, pady=15)

        desLbl = tk.Label(inFrame,text="Desease:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        desLbl.grid(row=3, column=0, padx=20, pady=15)
        self.desIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.desIn.grid(row=3, column=1, padx=10, pady=15)

        hpLbl = tk.Label(inFrame,text="Health Points:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        hpLbl.grid(row=4, column=0,padx=20, pady=15)
        self.hpIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.hpIn.grid(row=4, column=1, padx=10, pady=15)

        medLbl = tk.Label(inFrame,text="Medication:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        medLbl.grid(row=5, column=0, padx=20, pady=15)
        self.medIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.medIn.grid(row=5,column=1, padx=10, pady=15)

        addrLbl = tk.Label(inFrame,text="Address:", bg=self.clr(190,180,220),font=("Arial",15,"bold"))
        addrLbl.grid(row=6, column=0, padx=20, pady=15)
        self.addrIn = tk.Entry(inFrame, width=20, bd=2, font=("Arial",15))
        self.addrIn.grid(row=6, column=1, padx=10, pady=15)

        okBtn = tk.Button(inFrame, text="Admit",command=self.insertFun, bd=2, relief="raised", bg="gray", font=("Arial",20,"bold"), width=20)
        okBtn.grid(padx=30, pady=25,columnspan=2)

        # detail Frame

        self.detFrame = tk.Frame(self.root, bd=4, relief="groove",bg=self.clr(190,220,180))
        self.detFrame.place(width=self.width/2+110, height=self.height-180, x=self.width/3+60,y=100)

        pIdLbl = tk.Label(self.detFrame, text="Patient ID:", bg=self.clr(190,220,180), font=("Arial",15))
        pIdLbl.grid(row=0, column=0, padx=10, pady=15)
        self.pIdIn = tk.Entry(self.detFrame, bd=1, width=12, font=("Arial",15))
        self.pIdIn.grid(row=0, column=1, padx=7, pady=15)

        medicBtn = tk.Button(self.detFrame,command=self.medicsFun, text="Medication",width=10,font=("Arial",15,"bold"), bd=2, relief="raised")
        medicBtn.grid(row=0, column=2,padx=8, pady=15)

        hpBtn = tk.Button(self.detFrame,command=self.hPointFun, text="H_Point",width=10,font=("Arial",15,"bold"), bd=2, relief="raised")
        hpBtn.grid(row=0, column=3,padx=8, pady=15)

        disBtn = tk.Button(self.detFrame,command=self.disFun, text="Discharge",width=10,font=("Arial",15,"bold"), bd=2, relief="raised")
        disBtn.grid(row=0, column=4,padx=8, pady=15)

        
        self.tabFun()

    def tabFun(self):
        self.tabFrame = tk.Frame(self.detFrame, bd=3, relief="ridge", bg="cyan")
        self.tabFrame.place(width=self.width/2+80, height=self.height-280, x=12, y=80)

        x_scrol=tk.Scrollbar(self.tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(self.tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(self.tabFrame,columns=("id","name","bGroup","desease","hPoint","medi","addr"),xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set)

        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("id", text="Patient_Id")
        self.table.heading("name", text="Patient Name")
        self.table.heading("bGroup", text="B_Group")
        self.table.heading("desease", text="Desease")
        self.table.heading("hPoint", text="Points")
        self.table.heading("medi", text="Medication")
        self.table.heading("addr", text="Patient Address")
        self.table["show"]= "headings"

        self.table.column("id", width=100)
        self.table.column("name", width=150)
        self.table.column("bGroup", width=100)
        self.table.column("desease", width=120)
        self.table.column("hPoint", width=60)
        self.table.column("medi", width=150)
        self.table.column("addr", width=200)

        self.table.pack(fill="both", expand=1)

    def clr(self, r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def insertFun(self):
        id = int(self.idIn.get())
        name = self.nameIn.get()
        bGroup = self.bgIn.get()
        desease = self.desIn.get()
        point = int(self.hpIn.get())
        medics = self.medIn.get()
        addr = self.addrIn.get()

        if id and name and bGroup and desease and point and medics and addr:

            try:
                self.dbFun()
                query = f"insert into hospital (id,name,b_group,desease,h_points,medication,addr) values(%s,%s,%s,%s,%s,%s,%s)"
                self.cur.execute(query,(id,name,bGroup,desease,point,medics,addr))
                self.con.commit()
                self.tabFun()
                self.table.delete(*self.table.get_children())
                self.cur.execute("select * from hospital where id=%s",id)
                data = self.cur.fetchone()
                self.table.insert('',tk.END,values=data)
                tk.messagebox.showinfo("Success",f"Patient {name} is admitted!")
                self.con.close()
                self.clearFun()

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            tk.messagebox.showerror("Error","Fill All Input Fields!")


    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="admin", database="rec")
        self.cur = self.con.cursor()

    def clearFun(self):
        self.idIn.delete(0,tk.END)
        self.nameIn.delete(0,tk.END)
        self.bgIn.delete(0,tk.END)
        self.desIn.delete(0,tk.END)
        self.hpIn.delete(0,tk.END)
        self.medIn.delete(0,tk.END)
        self.addrIn.delete(0,tk.END)

    def medicsFun(self):
        pId = int(self.pIdIn.get())
        if pId:
            try:
                self.dbFun()
                query = f"select * from hospital where id=%s"
                self.cur.execute(query,pId)
                data = self.cur.fetchone()
                self.tabFun()
                self.table.delete(*self.table.get_children())
                self.table.insert('',tk.END,values=data)


            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            tk.messagebox.showerror("Error","Must Enter Patient ID")

    def hPointFun(self): 
        self.pointFrame=tk.Frame(self.root, bg="light gray", bd=3, relief="ridge")
        self.pointFrame.place(width=400, height=150,x=500, y=200)

        lbl = tk.Label(self.pointFrame, text="Enter Point:", bg="light gray", font=("Arial",15,"bold"))
        lbl.grid(row=0, column=0, padx=20, pady=20)
        self.pointIn = tk.Entry(self.pointFrame, width=17, bd=2,font=("Arial",15,"bold"))
        self.pointIn.grid(row=0, column=1, padx=10, pady=20)

        okBtn = tk.Button(self.pointFrame,command=self.addPoint, text="Add Point", bd=3, relief="raised",font=("Arial",20,"bold"),width=20)
        okBtn.grid(row=1, column=0, padx=30, pady=20,columnspan=2)

    def addPoint(self):
        pId = int(self.pIdIn.get())
        point = int(self.pointIn.get())
        if pId:
            try:
                self.dbFun()
                query = f"select h_points from hospital where id=%s"
                self.cur.execute(query,pId)
                val = self.cur.fetchone()

                newPoint = val[0]+point
                query2 = f"update hospital set h_points=%s where id=%s"
                self.cur.execute(query2,(newPoint,pId))
                self.con.commit()
                self.tabFun()
                self.table.delete(*self.table.get_children())
                self.cur.execute("select * from hospital where id=%s", pId)
                row = self.cur.fetchone()
                self.table.insert('',tk.END,values=row)
                tk.messagebox.showinfo("Success",f"Health Position is updated for patien {pId}") 
                self.con.close()
                self.pointFrame.destroy()                                         
                              

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

        else:
            tk.messagebox.showerror("Error","Must Enter Patient ID")
    def disFun(self):
        pId = int(self.pIdIn.get())
        try:
            self.dbFun()
            query = f"delete from hospital where id =%s"
            self.cur.execute(query,pId)
            self.con.commit()
            tk.messagebox.showinfo("Success",f"Patient {pId} is Dischared from Hospital")

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")


root = tk.Tk()
obj = hospital(root)
root.mainloop()