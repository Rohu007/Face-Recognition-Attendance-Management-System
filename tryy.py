from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        self.var_ename = StringVar()
        self.var_passname = StringVar()
        
        frs_frame = Frame(self.root, bg="#01454c")
        frs_frame.place(x=0, y=0, width=1280, height=100)
        
        frs_label = Label(frs_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM", fg="White", bg="#015b66", font=("Latin", 30, "bold"))
        frs_label.place(x=10, y=10, width=1260, height=80)
        
        main_frame = Frame(self.root, bg="#01454c")
        main_frame.place(x=0, y=100, width=1280, height=600)
        
        sub_frame = Frame(main_frame, bg="#04163a")
        sub_frame.place(x=10, y=10, width=1260, height=570)
        
        btm_frame = Frame(sub_frame, bg="#04163a")
        btm_frame.place(x=0, y=520, width=1260, height=50)
        
        term_label = Label(btm_frame, text="Terms & Condition", fg="White", bg="#04163a", font=("Lucida Fax", 10, "bold"))
        term_label.pack(side=BOTTOM)
        
        login_frame = Frame(sub_frame, bg="#015b66")
        login_frame.place(x=430, y=60, width=400, height=450)
        
        log_img = Image.open(r"C:\VS Code\Face Recognition Attendance System Project\photos\login_logo.png")
        log_img = log_img.resize((100, 100))
        self.photologimg = ImageTk.PhotoImage(log_img)
        
        log_lbl = Label(login_frame, image=self.photologimg, bg="#015b66")
        log_lbl.place(x=150, y=10, width=100, height=100)
        
        lookin_img = Image.open(r"C:\VS Code\Face Recognition Attendance System Project\photos\LookIn.png")
        lookin_img = lookin_img.resize((150, 50))
        self.photolookin = ImageTk.PhotoImage(lookin_img)
        
        lookin_lbl = Label(login_frame, image=self.photolookin, bg="#015b66")
        lookin_lbl.place(x=130, y=110, width=150, height=50)
        
        username = Label(login_frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        username.place(x=50, y=150)
        
        self.txtuser = ttk.Entry(login_frame, font=("times new roman", 16, "bold"))
        self.txtuser.place(x=50, y=180, width=270)
        
        password = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        password.place(x=50, y=220)
        
        self.txtpass = ttk.Entry(login_frame, font=("time new roman", 16, "bold"), show="*")
        self.txtpass.place(x=50, y=250, width=270)
        
        loginbtn = Button(login_frame, text="Login", font=("time new roman", 13, "bold"), bd=3, relief=RIDGE, fg="white", bg="#04163a", activeforeground="white", activebackground="#015b66", command=self.Login)
        loginbtn.place(x=110, y=310, width=145, height=30)
        
        registerbtn = Button(login_frame, text=" Register New User", command=self.register_window, font=("time new roman", 11, "bold"), borderwidth=0, fg="white", bg="#015b66", activeforeground="white", activebackground="#015b66")
        registerbtn.place(x=80, y=400, width=210, height=18)
        
        forgetbtn = Button(login_frame, text="Forget Password", font=("time new roman", 11, "bold"), borderwidth=0, fg="white", bg="#015b66", activeforeground="white", activebackground="#015b66", command=self.forgot_password_window)
        forgetbtn.place(x=80, y=370, width=210, height=18)
        
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_window(self.new_window)

    def Login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get().lower() == "rohit" and self.txtpass.get().lower() == "wish":
            messagebox.showinfo("Success", "Face Recognition System")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Rohit0758", database="register_data")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from login_data where email=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
                
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Invalid", "Invalid username or password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only admin")
                    if open_main > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                    else:
                        return
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Rohit0758", database="register_data")
            my_cursor = conn.cursor()
            query = ("select * from login_data where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("My Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l = Label(self.root2, text="Forget Password", font=("times new roman", 12, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)
                
                ScName_frame = Label(self.root2, text="Security Question", font=("Lucida Fax", 13, "bold"), fg="white", bg="#015b66")
                ScName_frame.place(x=50, y=80)
                
                self.combo_secu_que = ttk.Combobox(self.root2, font=("times new roman", 13), state="readonly")
                self.combo_secu_que["values"] = ("Select", "Your Birth Place", "Your best Friend", "Your Favorite Movie")
                self.combo_secu_que.place(x=50, y=110, width=180)
                self.combo_secu_que.current(0)
                
                AnsName_frame = Label(self.root2, text="Security Answer", font=("Lucida Fax", 13, "bold"), fg="white", bg="#015b66")
                AnsName_frame.place(x=50, y=150)
                
                self.txt_secu_ans = ttk.Entry(self.root2, font=("times new roman", 13))
                self.txt_secu_ans.place(x=50, y=180, width=180)
                
                NewPass_frame = Label(self.root2, text="New Password", font=("Lucida Fax", 13, "bold"), fg="white", bg="#015b66")
                NewPass_frame.place(x=50, y=220)
                
                self.txt_new_pass = ttk.Entry(self.root2, font=("times new roman", 13))
                self.txt_new_pass.place(x=50, y=250, width=180)
                
                btn = Button(self.root2, text="Reset", font=("times new roman", 13, "bold"), fg="white", bg="#04163a", activeforeground="white", activebackground="#015b66", command=self.reset_pass)
                btn.place(x=110, y=290)

    def reset_pass(self):
        if self.combo_secu_que.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question", parent=self.root2)
        elif self.txt_secu_ans.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Rohit0758", database="register_data")
            my_cursor = conn.cursor()
            query = ("select * from login_data where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_secu_que.get(), self.txt_secu_ans.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Please enter the correct Answer", parent=self.root2)
            else:
                query = ("update login_data set password=%s where email=%s")
                value = (self.txt_new_pass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Successfully your password has been reset, please login with new Password", parent=self.root2)
                self.root2.destroy()

class Register_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Register")

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_SecurityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        bg_frame = Frame(self.root, bg="#01454c")
        bg_frame.place(x=0, y=0, width=1600, height=900)

        register_frame = Frame(bg_frame, bg="#01454c")
        register_frame.place(x=260, y=90, width=800, height=600)

        register_label = Label(register_frame, text="REGISTER", font=("times new roman", 20, "bold"), fg="white", bg="#015b66")
        register_label.place(x=20, y=20)

        first_name = Label(register_frame, text="First Name", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        first_name.place(x=50, y=100)

        self.fname_entry = ttk.Entry(register_frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=130, width=250)

        last_name = Label(register_frame, text="Last Name", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        last_name.place(x=370, y=100)

        self.lname_entry = ttk.Entry(register_frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.lname_entry.place(x=370, y=130, width=250)

        contact = Label(register_frame, text="Contact No", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        contact.place(x=50, y=180)

        self.contact_entry = ttk.Entry(register_frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.contact_entry.place(x=50, y=210, width=250)

        email = Label(register_frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        email.place(x=370, y=180)

        self.email_entry = ttk.Entry(register_frame, textvariable=self.var_email, font=("times new roman", 15))
        self.email_entry.place(x=370, y=210, width=250)

        security_Q = Label(register_frame, text="Select Security Question", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        security_Q.place(x=50, y=260)

        self.combo_security_Q = ttk.Combobox(register_frame, textvariable=self.var_SecurityQ, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend", "Your Favorite Movie")
        self.combo_security_Q.place(x=50, y=290, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(register_frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        security_A.place(x=370, y=260)

        self.security_A_entry = ttk.Entry(register_frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.security_A_entry.place(x=370, y=290, width=250)

        password = Label(register_frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        password.place(x=50, y=340)

        self.password_entry = ttk.Entry(register_frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.password_entry.place(x=50, y=370, width=250)

        conf_password = Label(register_frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="white", bg="#015b66")
        conf_password.place(x=370, y=340)

        self.conf_password_entry = ttk.Entry(register_frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.conf_password_entry.place(x=370, y=370, width=250)

        register_btn = Button(register_frame, text="Register", font=("times new roman", 13, "bold"), bd=3, relief=RIDGE, fg="white", bg="#04163a", activeforeground="white", activebackground="#015b66", command=self.register_data)
        register_btn.place(x=100, y=450, width=145, height=35)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_SecurityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields are Required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        else:
            conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Rohit0758", database="register_data")
            my_cursor = conn.cursor()
            query = ("select * from login_data where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist, Please try another Email")
            else:
                my_cursor.execute("insert into login_data values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_SecurityQ.get(),
                    self.var_SecurityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered Successfully")

if __name__ == "__main__":
    main()













# from tkinter import *
# from tkinter import ttk, messagebox
# import mysql.connector

# class Login_window:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1600x900+0+0")
#         self.root.title("Login")

#         bg_frame = Frame(self.root, bg="#01454c")
#         bg_frame.place(x=0, y=0, width=1600, height=900)

#         login_frame = Frame(bg_frame, bg="#01454c")
#         login_frame.place(x=300, y=100, width=800, height=600)

#         login_label = Label(login_frame, text="LOGIN", font=("Lucida Fax", 20, "bold"), fg="white", bg="#015b66")
#         login_label.place(x=20, y=20)

#         email_label = Label(login_frame, text="Email", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         email_label.place(x=50, y=100)

#         self.email_entry = ttk.Entry(login_frame, font=("times new roman", 15))
#         self.email_entry.place(x=50, y=130, width=250)

#         password_label = Label(login_frame, text="Password", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         password_label.place(x=50, y=180)

#         self.password_entry = ttk.Entry(login_frame, font=("times new roman", 15), show="*")
#         self.password_entry.place(x=50, y=210, width=250)

#         login_btn = Button(login_frame, text="Login", font=("times new roman", 13, "bold"), bd=3, relief=RIDGE, fg="white", bg="#04163a", activeforeground="white", activebackground="#015b66", command=self.login)
#         login_btn.place(x=50, y=260, width=145, height=35)

#         register_btn = Button(login_frame, text="Register", font=("times new roman", 13, "bold"), bd=3, relief=RIDGE, fg="white", bg="#04163a", activeforeground="white", activebackground="#015b66", command=self.register_window)
#         register_btn.place(x=220, y=260, width=145, height=35)

#     def login(self):
#         if self.email_entry.get() == "" or self.password_entry.get() == "":
#             messagebox.showerror("Error", "All fields are required")
#         else:
#             conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Rohit0758", database="register_data")
#             my_cursor = conn.cursor()
#             my_cursor.execute("select * from login_data where email=%s and password=%s", (
#                 self.email_entry.get(),
#                 self.password_entry.get()
#             ))
#             row = my_cursor.fetchone()
#             if row is None:
#                 messagebox.showerror("Error", "Invalid Email & Password")
#             else:
#                 messagebox.showinfo("Success", "Login Successful")
#             conn.close()

#     def register_window(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Register_window(self.new_window)


# class Register_window:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1600x900+0+0")
#         self.root.title("Register")

#         self.var_fname = StringVar()
#         self.var_lname = StringVar()
#         self.var_contact = StringVar()
#         self.var_email = StringVar()
#         self.var_SecurityQ = StringVar()
#         self.var_SecurityA = StringVar()
#         self.var_pass = StringVar()
#         self.var_confpass = StringVar()

#         bg_frame = Frame(self.root, bg="#01454c")
#         bg_frame.place(x=0, y=0, width=1600, height=900)

#         register_frame = Frame(bg_frame, bg="#01454c")
#         register_frame.place(x=300, y=100, width=800, height=600)

#         register_label = Label(register_frame, text="REGISTER", font=("Lucida Fax", 20, "bold"), fg="white", bg="#015b66")
#         register_label.place(x=20, y=20)

#         first_name = Label(register_frame, text="First Name", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         first_name.place(x=50, y=100)

#         self.fname_entry = ttk.Entry(register_frame, textvariable=self.var_fname, font=("times new roman", 15))
#         self.fname_entry.place(x=50, y=130, width=250)

#         last_name = Label(register_frame, text="Last Name", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         last_name.place(x=370, y=100)

#         self.lname_entry = ttk.Entry(register_frame, textvariable=self.var_lname, font=("times new roman", 15))
#         self.lname_entry.place(x=370, y=130, width=250)

#         contact = Label(register_frame, text="Contact No", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         contact.place(x=50, y=180)

#         self.contact_entry = ttk.Entry(register_frame, textvariable=self.var_contact, font=("times new roman", 15))
#         self.contact_entry.place(x=50, y=210, width=250)

#         email = Label(register_frame, text="Email", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         email.place(x=370, y=180)

#         self.email_entry = ttk.Entry(register_frame, textvariable=self.var_email, font=("times new roman", 15))
#         self.email_entry.place(x=370, y=210, width=250)

#         security_Q = Label(register_frame, text="Select Security Question", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         security_Q.place(x=50, y=260)

#         self.combo_security_Q = ttk.Combobox(register_frame, textvariable=self.var_SecurityQ, font=("times new roman", 15), state="readonly")
#         self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Best Friend", "Your Favorite Movie")
#         self.combo_security_Q.place(x=50, y=290, width=250)
#         self.combo_security_Q.current(0)

#         security_A = Label(register_frame, text="Security Answer", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         security_A.place(x=370, y=260)

#         self.security_A_entry = ttk.Entry(register_frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
#         self.security_A_entry.place(x=370, y=290, width=250)

#         password = Label(register_frame, text="Password", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         password.place(x=50, y=340)

#         self.password_entry = ttk.Entry(register_frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
#         self.password_entry.place(x=50, y=370, width=250)

#         conf_password = Label(register_frame, text="Confirm Password", font=("Lucida Fax", 15, "bold"), fg="white", bg="#015b66")
#         conf_password.place(x=370, y=340)

#         self.conf_password_entry = ttk.Entry(register_frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
#         self.conf_password_entry.place(x=370, y=370, width=250)

#         register_btn = Button(register_frame, text="Register", font=("times new roman", 13, "bold"), bd=3, relief=RIDGE, fg="white", bg="#04163a", activeforeground="white", activebackground="#015b66", command=self.register_data)
#         register_btn.place(x=200, y=450, width=145, height=35)

#     def register_data(self):
#         if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_SecurityQ.get() == "Select":
#             messagebox.showerror("Error", "All Fields are Required")
#         elif self.var_pass.get() != self.var_confpass.get():
#             messagebox.showerror("Error", "Password & Confirm Password must be same")
#         else:
#             conn = mysql.connector.connect(host="127.0.0.1", username="root", password="Rohit0758", database="register_data")
#             my_cursor = conn.cursor()
#             query = ("select * from login_data where email=%s")
#             value = (self.var_email.get(),)
#             my_cursor.execute(query, value)
#             row = my_cursor.fetchone()
#             if row is not None:
#                 messagebox.showerror("Error", "User already exist, Please try another Email")
#             else:
#                 my_cursor.execute("insert into login_data values(%s,%s,%s,%s,%s,%s,%s)", (
#                     self.var_fname.get(),
#                     self.var_lname.get(),
#                     self.var_contact.get(),
#                     self.var_email.get(),
#                     self.var_SecurityQ.get(),
#                     self.var_SecurityA.get(),
#                     self.var_pass.get()
#                 ))
#                 conn.commit()
#                 conn.close()
#                 messagebox.showinfo("Success", "Registered Successfully")

# if __name__ == "__main__":
#     root = Tk()
#     app = Login_window(root)
#     root.mainloop()
