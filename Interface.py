from tkinter import *
from PIL import ImageTk
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1099x600+100+50")

        #Background Image
        self.bg=ImageTk.PhotoImage(file="images/58.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


root = Tk()
obj = Login(root)
root.mainloop()
