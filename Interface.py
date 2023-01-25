from tkinter import *

class Login:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1099x600+100+50")
        self.root.resizable(False, False)

        #Background Image
        self.bg=PhotoImage(file="images/Hela1.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=10, y=0, relwidth=1, relheight=1)

        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=100, width=400, height=400)

        #Title & subtitle
        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="black", bg="white").place(x=30,y=30)
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 16, "bold"), fg="#1d1d1d", bg="white").place(x=30,y=100)

        #Username
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 13, "bold"), fg="grey", bg="white").place(x=30,y=150)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=30, y=180, width=320, height=35)

        #Password
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 13, "bold"), fg="grey", bg="white").place(x=30, y=220)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=30, y=250, width=320, height=35)

        #CheckButton
        self.checkvalue = IntVar
        self.checkbtn = Checkbutton(Frame_login, text="Confirm", variable = self.checkvalue) 
        self.checkbtn.place(x=30, y=300)

        def getvals():
            print("Accepted")

        #SubmitButton
        Button(Frame_login, text="Submit", command=getvals).place(x=30, y=340)

root = Tk()
obj = Login(root)
root.mainloop()
