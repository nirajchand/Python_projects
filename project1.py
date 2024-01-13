from tkinter import*
class hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital managemant system")
        self.root.geometry("1540x800+0+0")
        Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="pink",bg="white",font=("times new roman",40,"bold")).pack(side=TOP,fill=X)


        #===========data frame======================
        Dataframe = Frame(self.root,bd = 20,relief = RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        

        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="patient information")
        Dataframeleft.place(x=0,y=5,width=980,height=350)

        Dataframeright = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new romen",12,"bold"),text="Prescription")
        Dataframeright.place(x=990,y=5,width=460,height=350)







root = Tk()
ob = hospital(root)
root.mainloop()