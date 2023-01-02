from tkinter import *
from PIL import Image, ImageTk # pip install pillow

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #####################1st img##############################
        img1 = Image.open("images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root, image = self.photoimg1, bd = 4,\
                       relief = RIDGE)
        lbling.place(x=0, y=0, width = 1550, height = 140)

        #####################Logo##############################
        img2 = Image.open("images\logohotel.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image = self.photoimg2, bd = 4,\
                       relief = RIDGE)
        lbling.place(x=0, y=0, width = 230, height = 140)

        #####################Title##############################
        lbl_title = Label(self.root, text = "Hotel Management System",\
        font = ("times new roman", 40, "bold"), bg = "black", fg = "gold",\
        bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 140, width = 1550, height = 50)

if __name__ == '__main__':
    root = Tk()
    project = HotelManagementSystem(root)
    root.mainloop()