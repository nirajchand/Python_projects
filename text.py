# from tkinter import *
# root = Tk()
# root.title("Niraj")

# root.eval('Tk::placewindow.center')
# c = Canvas(root,bg = "yellow",height = 250,width = 300)

# line = c.create_line(108, 120, 320, 40, fill = "green")
# arc = c.create_arc(180, 150, 80, 210, start = 0, extent = 220, fill="red")
# oval = c.create_oval(100, 30, 140, 150, fill ="blue")
# c.pack()

# root.mainloop()




# from tkinter import *
# root = Tk()
# root.title("Menu setting")
# root.geometry("650x320")
# menubutton = Menubutton(root, text="Menu")
# menubutton.menu = Menu(menubutton)
# menubutton["menu"] = menubutton.menue

# menubutton.menu.add_checkbutton(label="setting", variable=IntVar())
# menubutton.menu.add_checkbutton(label="Language",variable=IntVar())
# menubutton.menu.add_checkbutton(label="control",variable=IntVar())
# menubutton.pack()


# root.mainloop()



# from tkinter import *
# root = Tk()

# root.title("menu button")
# root.geometry("650x320")
# Label(root,text="Menu setting",fg="red").pack()

# a = Menubutton(root, text="MENU",bg="Green",fg="YEllow")

# a.menu = Menu(a)
# a["menu"] = a.menu

# a.menu.add_checkbutton(label="Dal bhat", variable=IntVar())
# a.menu.add_checkbutton(label="Roti", variable=IntVar())
# a.menu.add_checkbutton(label="Momo", variable=IntVar())
# a.pack()


# root.mainloop()



# from tkinter import *
# root = Tk()
# root.geometry("650x350")

# message_box = Message(root,text="How is your life going")
# message_box.pack(side=TOP)


# root.mainloop()


# from tkinter import *
# def select():
#     selection = "you selected the option "+str(var.get())
#     label.config(text=selection)
# root = Tk()
# root.geometry("650x300")
# var = IntVar()
# R1 = Radiobutton(root, text="Male",variable=var,value=1,command=select)
# R1.pack()
# R2 = Radiobutton(root,text="Female",variable=var,value=2,command=select)
# R2.pack()
# label = Label(root)
# label.pack()


# root.mainloop()


# from tkinter import *
# root = Tk()
# root.geometry("650x320")
# scrollbar= Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)

# mylist = Listbox(root, yscrollcommand= scrollbar.set)

# for line in range(100):
#     mylist.insert(END,"This is line number"+ str(line))

# mylist.pack(side=LEFT,fill=BOTH)
# scrollbar.config(command=mylist.yview)

# root.mainloop()





# from tkinter import *

# def frame():
#    Label(root,text="Welcome to Multiplication section",font=20).grid(row=6,column=4)
#    a = Menubutton(root,text="Multiplication Table ",bg= "yellow")
#    a.grid(row=7,column=3)
#    a.menu = Menu(a)
#    a["menu"] = a.menu

#    for i in range(1,11):
#         a.menu.add_checkbutton(label=i,command=lambda i=i: table(i))
# def table(value):
#     Label(root, text=f"Multiplication table of {value} is: \n").grid(row=8,column=0)
#     for multi in range(1,11):
#         total = value*multi
#         Label(root, text=f"{value}*{multi} = {total}").grid(row=9+multi,column=3)
#         Label(root,text="Thank you for using",font=30, fg="green").grid(row=21,column=3)
# def close_window():
#     root.destroy()

# root = Tk()
# root.title("Maths")
# root.geometry("700x300")

# Label(root, text="MATHS",bg="red").grid(row=0,column=4)

# Label(root,text="User Id: ").grid(row=1,column=2)
# Label(root,text="Password: ").grid(row=2,column=2)
# Entry(root, textvariable=IntVar()).grid(row=1,column=3)
# Entry(root, textvariable=IntVar()).grid(row=2,column=3)

# Button(root,text="Login",bg="blue",command=frame).grid(row=3,column=3)
# Button(root,text="Close window",bg="red",command=close_window).grid(row=3,column=8)

# root.mainloop()





# from tkinter import *
# root = Tk()
# root.geometry("650x200")
# root.eval('tk::PlaceWindow . Center')

# text = Text(root)
# text.insert(INSERT,"My name is niraj chand.")
# text.insert(END,"You are handsome.")

# text.tag_add("text1","1.11","1.22")
# text.tag_add("text2","1.31","1.39")

# text.tag_config("text1",background="green")
# text.tag_config("text2",background="red")
# text.pack()

# root.mainloop()















































