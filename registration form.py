from tkinter import *
from webbrowser import BackgroundBrowser
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text= "New Employee IT Requirements", font="ar 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="Name")
epf = Label(root, text="Epf")
department = Label(root, text="Department")
designation = Label(root, text="Designation")
needsim = Label(root, text="Need Sim")
needlaptop = Label(root, text="Need Laptop")
needmail = Label(root, text="Need Mail")

#Packing Fields
name.grid(row=1, column=2)
epf.grid(row=2, column=2)
department.grid(row=3, column=2)
designation.grid(row=4, column=2)
needsim.grid(row=5, column=2)
needlaptop.grid(row=6, column=2)
needmail.grid(row=7, column=2)

#Variable for storing data
namevalue = StringVar
epfvalue = StringVar
departmentvalue = StringVar
designationvalue = StringVar
needsimvalue = StringVar
needlaptopvalue = StringVar
needmailvalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable =namevalue)
epfentry = Entry(root, textvariable =epfvalue)
departmententry = Entry(root, textvariable =departmentvalue)
designationentry = Entry(root, textvariable =designationvalue)
needsimentry = Entry(root, textvariable =needsimvalue)
needlaptopentry = Entry(root, textvariable =needlaptopvalue)
needmailentry = Entry(root, textvariable =needmailvalue)

#Packing entry fields
nameentry.grid(row =1, column =3 )
epfentry.grid(row =2, column =3 )
departmententry.grid(row =3, column =3 )
designationentry.grid(row =4, column =3 )
needsimentry.grid(row =5, column =3 )
needlaptopentry.grid(row =6, column =3 )
needmailentry.grid(row =7, column =3 )

#Creating Checkbox
checkbtn = Checkbutton(text="Confirm", variable = checkvalue)
checkbtn.grid(row=8, column=3)

#Submit Button
Button(text="Submit", command=getvals).grid(row=9, column=3)


root.mainloop()
