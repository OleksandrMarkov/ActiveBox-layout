from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk
import sqlite3
import random
from tkinter import messagebox

class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #####################Variables##############################
        self.var_ref = StringVar()
        x = random.randint(1000, 9999) # [1000; 9999]
        self.var_ref.set(str(x))

        self.var_customer_name = StringVar()
        self.var_mother_name = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

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

        entry_ref = ttk.Entry(label_frame_left, textvariable = self.var_ref, width = 29,\
        state = "readonly", font = ("times new roman", 13, "bold"))
        entry_ref.grid(row = 0, column = 1)

        # customer name
        customer_name = Label(label_frame_left, text = "Customer Name:",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        customer_name.grid(row = 1, column = 0, sticky = W)

        entry_customer_name = ttk.Entry(label_frame_left, textvariable = self.var_customer_name,
        width = 29, font = ("times new roman", 13, "bold"))
        entry_customer_name.grid(row = 1, column = 1)

        # mother name
        label_mother_name = Label(label_frame_left, text = "Mother name:",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_mother_name.grid(row = 2, column = 0, sticky = W)

        entry_mother_name = ttk.Entry(label_frame_left, textvariable = self.var_mother_name, width = 29,
        font = ("times new roman", 13, "bold"))
        entry_mother_name.grid(row = 2, column = 1)

        # gender
        label_gender = Label(label_frame_left, text = "Gender:",\
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_gender.grid(row = 3, column = 0, sticky = W)

        combobox_gender = ttk.Combobox(label_frame_left, textvariable = self.var_gender,
        font = ("times new roman", 12, "bold"),\
        width = 31, state="readonly")
        combobox_gender["value"] = ("Male", "Female", "None")
        combobox_gender.current(0)
        combobox_gender.grid(row=3, column=1)

        # postcode
        label_postcode = Label(label_frame_left, text = "Postcode:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_postcode.grid(row = 4, column = 0, sticky = W)

        entry_postcode = ttk.Entry(label_frame_left, textvariable = self.var_postcode, width = 29,
        font = ("times new roman", 13, "bold"))
        entry_postcode.grid(row = 4, column = 1)

        # mobile number
        label_mobile = Label(label_frame_left, text = "Mobile:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_mobile.grid(row = 5, column = 0, sticky = W)

        entry_mobile = ttk.Entry(label_frame_left, textvariable = self.var_mobile, width = 29,
        font = ("times new roman", 13, "bold"))
        entry_mobile.grid(row = 5, column = 1)

        # email
        label_email = Label(label_frame_left, text = "Email:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_email.grid(row = 6, column = 0, sticky = W)

        entry_email = ttk.Entry(label_frame_left, textvariable = self.var_email, width = 29,
        font = ("times new roman", 13, "bold"))
        entry_email.grid(row = 6, column = 1)

        # nationality
        label_nationality = Label(label_frame_left, text="Nationality:", \
        font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_nationality.grid(row=7, column=0, sticky=W)

        combobox_nation = ttk.Combobox(label_frame_left, textvariable = self.var_nationality,
        font=("times new roman", 12, "bold"), width=31, state="readonly")
        combobox_nation["value"] = ("Ukrainian", "Polish", "Romanian")
        combobox_nation.current(0)
        combobox_nation.grid(row=7, column=1)

        # id proof
        label_id_proof = Label(label_frame_left, text="ID Proof Type:", \
        font=("times new roman", 12, "bold"), padx=2, pady=6)
        label_id_proof.grid(row=8, column=0, sticky=W)

        combobox_id_proof = ttk.Combobox(label_frame_left, textvariable = self.var_id_proof,
        font=("times new roman", 12, "bold"), width=31, state="readonly")
        combobox_id_proof["value"] = ("Passport", "Driving Licence", "Сredential")
        combobox_id_proof.current(0)
        combobox_id_proof.grid(row=8, column=1)

        # id number
        label_id_number = Label(label_frame_left, text = "ID Number:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_id_number.grid(row = 9, column = 0, sticky = W)

        entry_id_number = ttk.Entry(label_frame_left, textvariable = self.var_id_number, width = 29,
        font = ("times new roman", 13, "bold"))
        entry_id_number.grid(row = 9, column = 1)

        # address
        label_address = Label(label_frame_left, text = "Address:", \
        font = ("times new roman", 12, "bold"), padx = 2, pady = 6)
        label_address.grid(row = 10, column = 0, sticky = W)

        entry_address = ttk.Entry(label_frame_left, textvariable = self.var_address, width = 29,
        font = ("times new roman", 13, "bold"))
        entry_address.grid(row = 10, column = 1)

        ##################### Buttons ##############################

        btn_frame = Frame(label_frame_left, bd = 2, relief=RIDGE)
        btn_frame.place(x=0, y=400,width = 412, height=40)

        btn_add = Button(btn_frame, text="Add", command = self.add_data, font = ("times new roman", 12, "bold"),\
        width = 10, bg="black", fg="gold")
        btn_add.grid(row=0,column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", command = self.update, font=("times new roman", 12, "bold"), \
        width=10, bg="black", fg="gold")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", command = self.nDelete, font=("times new roman", 12, "bold"), \
        width=10, bg="black", fg="gold")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command = self.reset, font=("times new roman", 12, "bold"), \
        width=10, bg="black", fg="gold")
        btn_reset.grid(row=0, column=3, padx=1)

        ##################### Table frame ##############################
        table_frame = LabelFrame(self.root, bd = 2, relief = RIDGE,\
        text = "View Details and Search", font=("times new roman", 12, "bold"),\
                                      padx = 2, pady = 6)
        table_frame.place(x = 435, y = 50, width = 860, height = 490)

        label_search_by = Label(table_frame, text="Search by:", \
        font=("times new roman", 12, "bold"), bg = "red", fg="white")
        label_search_by.grid(row=0, column=0, sticky=W, padx = 2)

        combobox_search = ttk.Combobox(table_frame, font=("times new roman", 12, "bold"), \
        width=31, state="readonly")
        combobox_search["value"] = ("Mobile", "Ref")
        combobox_search.current(0)
        combobox_search.grid(row=0, column=1, padx = 2)

        entry_search = ttk.Entry(table_frame, width=31, font=("times new roman", 13, "bold"))
        entry_search.grid(row = 0, column = 2, padx = 2)

        btn_search = Button(table_frame, text="Search", font=("times new roman", 12, "bold"), \
        width=10, bg="black", fg="gold")
        btn_search.grid(row=0, column=3, padx=1)

        btn_show_all = Button(table_frame, text="Show all", font=("times new roman", 12, "bold"), \
        width=10, bg="black", fg="gold")
        btn_show_all.grid(row=0, column=4, padx=1)

        #####################Data table##############################
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.details_table = ttk.Treeview(details_table,\
        column = ("ref", "name", "mother", "gender", "post", "mobile", "email",
        "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("ref", text="Refer No")
        self.details_table.heading("name", text="Name")
        self.details_table.heading("mother", text="Mother")
        self.details_table.heading("gender", text="Gender")
        self.details_table.heading("post", text="PostCode")
        self.details_table.heading("mobile", text="Mobile")
        self.details_table.heading("email", text="Email")
        self.details_table.heading("nationality", text="Nationality")
        self.details_table.heading("idproof", text="ID Proof")
        self.details_table.heading("idnumber", text="ID Number")
        self.details_table.heading("address", text="Address")

        self.details_table["show"] = "headings"

        self.details_table.column("ref", width = 100)
        self.details_table.column("name", width=100)
        self.details_table.column("mother", width=100)
        self.details_table.column("gender", width=100)
        self.details_table.column("post", width=100)
        self.details_table.column("mobile", width=100)
        self.details_table.column("email", width=100)
        self.details_table.column("nationality", width=100)
        self.details_table.column("idproof", width=100)
        self.details_table.column("idnumber", width=100)
        self.details_table.column("address", width=100)

        self.details_table.pack(fill=BOTH, expand=1)
        self.details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = sqlite3.connect('hotel_management_system')
                cursor = conn.cursor()
                add_customer_query = f"INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?,?,?)"

                customer_parameters = (self.var_ref.get(), self.var_customer_name.get(), self.var_mother_name.get(),
                self.var_gender.get(), self.var_postcode.get(), self.var_mobile.get(), self.var_email.get(),
                self.var_nationality.get(), self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get())

                cursor.execute(add_customer_query, customer_parameters)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added!", parent = self.root)
            except Exception as ex:
                # print(add_customer_query)
                messagebox.showwarning("Warning", f"Something went wrong: {ex}", parent = self.root)

    def fetch_data(self): # 24:38
        try:
            conn = sqlite3.connect('hotel_management_system')
            cursor = conn.cursor()
            select_all_customers_query = """SELECT * FROM customers"""
            cursor.execute(select_all_customers_query)
            records = cursor.fetchall()
            if len(records) != 0:
                self.details_table.delete(*self.details_table.get_children())
                for i in records:
                    self.details_table.insert("", END, values = i)
                conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showwarning("Warning", f"Something went wrong: {ex}", parent=self.root)

    def get_cursor(self, event = ""):
        cursor_row = self.details_table.focus()
        content = self.details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_customer_name.set(row[1]),
        self.var_mother_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_postcode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        try:

            if self.var_mobile.get() == "":
                messagebox.showerror("Error", "Please enter mobile number", parent = self.root)
            else:
                conn = sqlite3.connect('hotel_management_system')
                cursor = conn.cursor()
                update_customer_query = """UPDATE customers SET name = ?, mother = ?, gender = ?, postcode = ?,
                  mobile = ?, email = ?, nationality = ?, id_proof = ?, id_number = ?, address = ? WHERE 
                  ref = ?"""
                customer_parameters = (self.var_customer_name.get(), self.var_mother_name.get(),
                self.var_gender.get(), self.var_postcode.get(), self.var_mobile.get(), self.var_email.get(),
                self.var_nationality.get(), self.var_id_proof.get(), self.var_id_number.get(), self.var_address.get(),
                self.var_ref.get())

                cursor.execute(update_customer_query, customer_parameters)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Customer details has been updated successfully!", parent = self.root)

        except Exception as ex:
            messagebox.showwarning("Warning", f"Something went wrong: {ex}", parent=self.root)

    def nDelete(self):
        nDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?",
        parent = self.root)

        if nDelete > 0:
            try:
                conn = sqlite3.connect('hotel_management_system')
                cursor = conn.cursor()
                delete_the_customer_query = "DELETE FROM customers WHERE ref = ?"
                value = (self.var_ref.get(),)
                cursor.execute(delete_the_customer_query, value)
            except:
                messagebox.showwarning("Warning", f"Something went wrong: {ex}", parent=self.root)
        else:
            if not nDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        x = random.randint(1000, 9999)  # [1000; 9999]
        self.var_ref.set(str(x))
        
        self.var_customer_name.set(""),
        self.var_mother_name.set(""),
        #self.var_gender.set(""),
        self.var_postcode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

if __name__ == '__main__':
    root = Tk()
    win = CustomerWindow(root)
    root.mainloop()