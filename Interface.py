from tkinter import *
from tkinter import messagebox
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
        Frame_login.place(x=0, y=100, width=400, height=500)

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
        self.checkbtn = Checkbutton(Frame_login, text="Confirm", cursor="hand2", variable = self.checkvalue) 
        self.checkbtn.place(x=30, y=300)


        #SubmitButton
        self.check_function = StringVar
        Button(Frame_login, text="forgot password?", bd=0, cursor="hand2", fg="black", bg="white").place(x=30, y=330), 
        Button(Frame_login, command=self.check_function, cursor="hand2", text="Submit", bg="black", fg="white").place(x=30, y=370)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() != "immanuelm" or self.password.get() != "123456":
            messagebox.showerror("Error", "Invalid Username or", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")


root = Tk()
obj = Login(root)
root.mainloop()
