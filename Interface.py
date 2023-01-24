from tkinter import *

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1099x600+100+50")
        self.root.resizable(False, False)

        #Background Image
        self.bg=PhotoImage(file="images/6.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=10, y=0, relwidth=1, relheight=1)

        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=250, y=100, width=600, height=400)



root = Tk()
obj = Login(root)
root.mainloop()
