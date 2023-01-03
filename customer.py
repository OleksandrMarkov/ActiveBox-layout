from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk

class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #####################Title##############################
        lbl_title = Label(self.root, text="Add customer details".upper(), \
        font=("times new roman", 18, "bold"), bg="black", fg="gold", \
        bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        #####################Logo##############################
        img2 = Image.open("images\logohotel.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image = self.photoimg2, bd = 0,\
        relief = RIDGE)
        lbling.place(x=5, y=2, width = 100, height = 40)

        #####################Label frame##############################
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE,\
        text = "Customer Details", font=("times new roman", 12, "bold"),\
                                      padx = 2, pady = 6)
        label_frame_left.place(x = 5, y = 50, width = 425, height = 490)

        #####################Labels, entries##############################

        # customer ref
        label_customer_ref = Label(label_frame_left, text = "Customer Ref",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_customer_ref.grid(row = 0, column = 0, sticky = W)

        entry_ref = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_ref.grid(row = 0, column = 1)

        # customer name
        customer_name = Label(label_frame_left, text = "Customer Name:",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        customer_name.grid(row = 1, column = 0, sticky = W)

        entry_customer_name = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_customer_name.grid(row = 1, column = 1)

        # mother name
        label_mother_name = Label(label_frame_left, text = "Mother name:",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_mother_name.grid(row = 2, column = 0, sticky = W)

        entry_mother_name = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_mother_name.grid(row = 2, column = 1)

        # gender
        label_gender = Label(label_frame_left, text = "Gender:",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_gender.grid(row = 3, column = 0, sticky = W)

        combobox_gender = ttk.Combobox(label_frame_left, font = ("times new roman", 12, "bold"),\
        width = 31, state="readonly")
        combobox_gender["value"] = ("Male", "Female", "None")
        combobox_gender.current(0)
        combobox_gender.grid(row=3, column=1)


        # postcode
        label_postcode = Label(label_frame_left, text = "Postcode:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_postcode.grid(row = 4, column = 0, sticky = W)

        entry_postcode = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_postcode.grid(row = 4, column = 1)

        # mobile number
        label_mobile = Label(label_frame_left, text = "Mobile:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_mobile.grid(row = 5, column = 0, sticky = W)

        entry_mobile = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_mobile.grid(row = 5, column = 1)

        # email
        label_email = Label(label_frame_left, text = "Email:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_email.grid(row = 6, column = 0, sticky = W)

        entry_email = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_email.grid(row = 6, column = 1)

        # nationality
        label_nationality = Label(label_frame_left, text="Nationality:", \
        font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_nationality.grid(row=7, column=0, sticky=W)

        combobox_nation = ttk.Combobox(label_frame_left, font=("times new roman", 12, "bold"), \
        width=31, state="readonly")
        combobox_nation["value"] = ("Ukrainian", "Polish", "Romanian")
        combobox_nation.current(0)
        combobox_nation.grid(row=7, column=1)

        # id proof
        label_id_proof = Label(label_frame_left, text="ID Proof Type:", \
        font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_id_proof.grid(row=8, column=0, sticky=W)

        combobox_id_proof = ttk.Combobox(label_frame_left, font=("times new roman", 12, "bold"), \
        width=31, state="readonly")
        combobox_id_proof["value"] = ("Passport", "Driving Licence", "Сredential")
        combobox_id_proof.current(0)
        combobox_id_proof.grid(row=8, column=1)

        # id number
        label_id_number = Label(label_frame_left, text = "ID Number:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_id_number.grid(row = 9, column = 0, sticky = W)

        entry_id_number = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_id_number.grid(row = 9, column = 1)

        # address
        label_address = Label(label_frame_left, text = "Address:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_address.grid(row = 10, column = 0, sticky = W)

        entry_address = ttk.Entry(label_frame_left, width = 29, font = ("times new roman", 13, "bold"))
        entry_address.grid(row = 10, column = 1)

if __name__ == '__main__':
    root = Tk()
    win = CustomerWindow(root)
    root.mainloop()