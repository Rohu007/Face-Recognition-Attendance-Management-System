from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student_Details:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognition System")
        
        #------------------------------------Variables-------------------------------------
        
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_enroll = StringVar()
        self.var_name = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        
        
        # ----------------------------------------Basic Frame Boundary---------------------------------------------
        
        
        #Frame for face recognition system label
        frs_frame = Frame(self.root , bg = "#01454c" )
        frs_frame.place(x=0 , y=0 , width=1280 , height=100)
        
        #Label for face recognition system 
        frs_label = Label(frs_frame , text="STUDENT DETAILS" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
        frs_label.place(x=10 , y=10 , width=1260 , height=80  )
        
        
        #Frame for main body
        main_frame = Frame(self.root , bg = "#01454c")
        main_frame.place(x=0 , y=100 , width=1280 , height=600)
        
        #Sub frame
        sub_frame = Frame(main_frame , bg = "#04163a")
        sub_frame.place(x=10 , y=10 , width=1260 , height=570)
  
  
#   ----------------------------------------------New GUI Boundary-----------------------------------------------

#                         --------------------------Left Frame---------------------------------

        #Left Frame
        left_frame = LabelFrame(sub_frame , bd=4 , relief=RIDGE , fg="White" , bg="#04163a" , text="Cource Information" , font=("Californian FB" , 12 , "bold"))
        left_frame.place(x=10 , y=10 , width=620 , height=130)
        
        
        # --------------Course Information------------------
        
        
        #Course name
        crs_lbl = Label(left_frame , text="Course Name" , fg="White" , bg="#04163a")
        crs_lbl.grid(row=0 , column=0 , padx=10 , pady=10)
        
        crs_box = ttk.Combobox(left_frame , textvariable=self.var_course , width=17 , state="readonly")
        crs_box["values"] = ("Select Course" , "B. Tech" , "M. Tech" , "B. Sc." , "M. Sc." , "B.A." , "M.A." , "B. Com" , "M. Com" , "MBA" , "LLB")
        crs_box.current(0)
        crs_box.grid(row=0 , column=1 , padx=10 , pady=10)
        
        #Department Name
        dept_lbl = Label(left_frame , text="Department Name" , fg="White" , bg="#04163a")
        dept_lbl.grid(row=1 , column=0 , padx=10 , pady=10)
        
        dept_box = ttk.Combobox(left_frame , textvariable=self.var_dep , width=17 , state="readonly")
        dept_box["values"] = ("Select Department" , "CSE" , "AIML" , "DS" , "AIDS" , "ME" , "CE" , "EE" , "ECE")
        dept_box.current(0)
        dept_box.grid(row=1 , column=1 , padx=10 , pady=10)
        
         #Academic Session
        sess_lbl = Label(left_frame , text="Academic Session" , fg="White" , bg="#04163a")
        sess_lbl.grid(row=0 , column=2 , padx=10 , pady=10)
        
        sess_box = ttk.Combobox(left_frame , textvariable=self.var_year , width=17 , state="readonly")
        sess_box["values"] = ("Select Session" , "2020-2021" , "2021-2022" , "2022-2023" , "2023-2024" , "2024-2025" , "2025-2026" , "2026-2027" , "2027-2028")
        sess_box.current(0)
        sess_box.grid(row=0 , column=3 , padx=10 , pady=10)
        
         #Semester
        sems_lbl = Label(left_frame , text="Current Semester" , fg="White" , bg="#04163a")
        sems_lbl.grid(row=1 , column=2 , padx=10 , pady=10)
        
        sems_box = ttk.Combobox(left_frame , textvariable=self.var_sem , width=17 , state="readonly")
        sems_box["values"] = ("Select Semester" , "Semester 1" , "Semester 2" , "Semester 3" , "Semester 4" , "Semester 5" , "Semester 6" , "Semester 7" , "Semester 8")
        sems_box.current(0)
        sems_box.grid(row=1 , column=3 , padx=10 , pady=10)
        
        
       #----------------------Inside Frame----------------------------
        
        
        #Inside Frame
        inleft_frame = LabelFrame(sub_frame , bd=4 , relief=RIDGE , fg="White" , bg="#04163a" , text="Student Information" , font=("Californian FB" , 12 , "bold"))
        inleft_frame.place(x=10 , y=150 , width=620 , height=410)
        
        
         #-----------------Student Information-----------------------
        
        
        #Enrollment Number
        enrl_lbl = Label(inleft_frame , text="Enrollment No" , fg="White" , bg="#04163a")
        enrl_lbl.grid(row=1 , column=0 , padx=10 , pady=10)
        
        enrl_ent = Entry(inleft_frame , textvariable=self.var_enroll , width=22)
        enrl_ent.grid(row=1 , column=1 , padx=10 , pady=10)
        
        #Student Name
        stu_lbl = Label(inleft_frame , text="Student Name" , fg="White" , bg="#04163a")
        stu_lbl.grid(row=1 , column=2 , padx=10 , pady=10)
        
        stu_ent = Entry(inleft_frame , textvariable=self.var_name , width=22)
        stu_ent.grid(row=1 , column=3 , padx=10 , pady=10)
        
        #Gender
        stu_lbl = Label(inleft_frame , text="Gender" , fg="White" , bg="#04163a")
        stu_lbl.grid(row=2 , column=0 , padx=10 , pady=10)
        
        gen_box = ttk.Combobox(inleft_frame , textvariable=self.var_gen , width=19 , state="readonly")
        gen_box["values"] = ("Select Gender" , "Male" , "Female" , "Prefer Not Say")
        gen_box.current(0)
        gen_box.grid(row=2 , column=1 , padx=10 , pady=10)
        
        
        #DOB
        stu_lbl = Label(inleft_frame , text="Date of Birth" , fg="White" , bg="#04163a")
        stu_lbl.grid(row=2 , column=2 , padx=10 , pady=10)
        
        stu_ent = Entry(inleft_frame , textvariable=self.var_dob , width=22)
        stu_ent.grid(row=2 , column=3 , padx=10 , pady=10)
        
        #Phone Number
        stu_lbl = Label(inleft_frame , text="Phone Number" , fg="White" , bg="#04163a")
        stu_lbl.grid(row=3 , column=0 , padx=10 , pady=10)
        
        stu_ent = Entry(inleft_frame , textvariable=self.var_phone , width=22)
        stu_ent.grid(row=3 , column=1 , padx=10 , pady=10)
        
        #E-mail
        stu_lbl = Label(inleft_frame , text="E-mail" , fg="White" , bg="#04163a")
        stu_lbl.grid(row=3 , column=2 , padx=10 , pady=10)
        
        stu_ent = Entry(inleft_frame , textvariable=self.var_email , width=22)
        stu_ent.grid(row=3 , column=3 , padx=10 , pady=10)
        
        
        #------------------Frame to take Sample Photo-----------------------------
        
        
        chota_frame = Frame(inleft_frame , bg="#04163a")
        chota_frame.place(x=0 , y=130 , width=600 , height=110)
        
        #photo sample pics
        #yes
        smplyes = Image.open(r"C:\VS Code\Face Recognition Attendance System Project\photos\photo sample yes.png")
        smplyes = smplyes.resize((80,80))
        self.photosmplyes = ImageTk.PhotoImage(smplyes)
        
        bttn4 = Button(chota_frame , image=self.photosmplyes)
        bttn4.place(x=150 , y=0 , width=80 , height=80)
        
        #photo sample pics
        #no
        smplno = Image.open(r"C:\VS Code\Face Recognition Attendance System Project\photos\photo sample no.png")
        smplno = smplno.resize((80,80))
        self.photosmplno = ImageTk.PhotoImage(smplno)
        
        bttn4 = Button(chota_frame , image=self.photosmplno)
        bttn4.place(x=400 , y=0 , width=80 , height=80)
        
        
        #Photo Sample Button
        
        self.var_radyn = StringVar()
        sampleyes = ttk.Radiobutton(chota_frame , variable=self.var_radyn, text="Photo" , value="YES" )
        sampleyes.place(x=150 , y=80 , width=80 , height=20)
        
        
        sampleno = ttk.Radiobutton(chota_frame , variable=self.var_radyn , text="No Photo" , value="NO" )
        sampleno.place(x=400 , y=80 , width=80 , height=20)
        
        
        #--------------------------Left frame 2------------------------------
        
        
        #Frame1 for Button to submit
        bttn1_frame = Frame(inleft_frame , bd=4 , bg="#04163a" , )
        bttn1_frame.place(x=10 , y=250 , width=590 , height=30)
        
         #Frame2 for Button to submit
        bttn2_frame = Frame(inleft_frame , bd=4 , bg="#04163a" , )
        bttn2_frame.place(x=10 , y=280 , width=590 , height=60)
        
         #Frame3 for Button to submit
        bttn3_frame = Frame(inleft_frame , bd=4 , bg="#04163a" , )
        bttn3_frame.place(x=10 , y=330 , width=590 , height=30)
        
        #Buttons
        
        #Take Photo sample
        tps_bttn = Button(bttn1_frame , command=self.generate_dataset ,  text="TAKE PHOTO SAMPLE" , width=81)
        tps_bttn.grid(row=0 , column=0 )
        
        #Save
        save_bttn = Button(bttn2_frame  , command=self.add_data , text="SAVE" , width=40)
        save_bttn.grid(row=0 , column=0 )
        
        #Update
        update_bttn = Button(bttn2_frame , command=self.update_data , text="UPDATE" , width=40)
        update_bttn.grid(row=0 , column=1 )
        
        #Delete
        delete_bttn = Button(bttn2_frame , command=self.delete_data , text="DELETE" , width=40)
        delete_bttn.grid(row=1 , column=0 )
        
        #Reset
        reset_bttn = Button(bttn2_frame , command=self.reset_data ,  text="RESET" , width=40)
        reset_bttn.grid(row=1 , column=1 )
        
        #Update Photo sample
        ups_bttn = Button(bttn3_frame , text="UPDATE PHOTO SAMPLE" , width=81)
        ups_bttn.grid(row=0 , column=0 )
        
        
        
        #                -----------------------Right Frame------------------------
        
        
        #Right Frame
        right_frame = LabelFrame(sub_frame , bd=4 , relief=RIDGE , fg="White" , bg="#04163a" , text="Search System" , font=("Californian FB" , 12 , "bold"))
        right_frame.place(x=640 , y=10 , width=615 , height=130)
  
        #Search By : how to search data
        srchby_lbl = Label(right_frame , text="Search by :" , bg="#04163a" , fg="White")
        srchby_lbl.grid(row=0 , column=0 , padx=10 , pady=10)
        
        srchby_box = ttk.Combobox(right_frame , width=17 , state="readonly")
        srchby_box["values"] = ("Select Semester" , "Enrollment Number" , "Department" , "Course")
        srchby_box.current(0)
        srchby_box.grid(row=0 , column=1 , padx=10 , pady=10)
        
        srch_ent = Entry(right_frame , width=20 )
        srch_ent.grid(row=0 , column=2 , padx=10 , pady=10)
  
        srch_bttn = Button(right_frame , text="SEARCH" , width=14 , padx=10 )
        srch_bttn.grid(row=1 , column=1 )
        
        showall_bttn = Button(right_frame , text="SHOW ALL" , width=14 , padx=10 )
        showall_bttn.grid(row=1 , column=2 )
  
    
        #                 ----------------Table Frame------------------
        
        
        table_frame = Frame(sub_frame , bd=4 , relief=RIDGE , bg="#04163a")
        table_frame.place(x=640 , y=160 , width=615 , height=400)
        
        scroll_x = ttk.Scrollbar(table_frame , orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame , orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame , columns=("enroll" , "name" , "dept" , "course" , "year" , "sem" , "phone" , "email" , "gen" , "dob" , "photo"))
        
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("enroll" , text="Enrollment Number")
        self.student_table.heading("name" , text="Student Name")
        self.student_table.heading("dept" , text="Department")
        self.student_table.heading("course" , text="Course")
        self.student_table.heading("year" , text="Academic Session")
        self.student_table.heading("sem" , text="Semester")
        self.student_table.heading("phone" , text="Phone Number")
        self.student_table.heading("email" , text="E-mail")
        self.student_table.heading("gen" , text="Gender")
        self.student_table.heading("dob" , text="DOB")
        self.student_table.heading("photo" , text="Photo Sample")
        self.student_table["show"] = "headings"
        
        self.student_table.pack(fill=BOTH , expand=1)
        self.student_table.bind("<ButtonRelease>" , self.get_cursor)
        self.fetch_data()
        
        
       
        
        
        
        
        #--------------------------------------Back-end Functions------------------------------------------
        
        
        
        #Save Data to the database
        
    def add_data(self):
        if self.var_course.get()=="Select Course" or self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Session" or self.var_sem.get()=="Select Semester" or self.var_enroll.get()=="" or self.var_name.get()=="" or self.var_gen.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_email.get()=="" :
            messagebox.showerror("Error" , "All Fields are Required" , parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "abhaytiwari@818" , database = "face_recognition" )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (
                                                                                                                    self.var_enroll.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_gen.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_radyn.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success" , "Student Details has been Added Successfully !" , parent=self.root)
            except Exception as es:
                messagebox.showerror("Error" , f"Due To : {str(es)}" , parent=self.root)
        
      
      
    #fetch data from the database
      
    def fetch_data(self):
        conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "abhaytiwari@818" , database = "face_recognition" )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from students")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("" , END , values=i)
            conn.commit()
        conn.close()
        
        
        
    #Get data by pointing and clicking cursor
    
    def get_cursor(self , event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_enroll.set(data[0]), 
        self.var_name.set(data[1]), 
        self.var_dep.set(data[2]), 
        self.var_course.set(data[3]), 
        self.var_year.set(data[4]), 
        self.var_sem.set(data[5]), 
        self.var_phone.set(data[6]), 
        self.var_email.set(data[7]), 
        self.var_gen.set(data[8]), 
        self.var_dob.set(data[9]), 
        self.var_radyn.set(data[10])
        
      
      
    #Update data in Database
    
    def update_data(self):
        if self.var_course.get()=="Select Course" or self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Session" or self.var_sem.get()=="Select Semester" or self.var_enroll.get()=="" or self.var_name.get()=="" or self.var_gen.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_email.get()=="" :
            messagebox.showerror("Error" , "All Fields are Required" , parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Update" , "Do you want to Update this Student Details" , parent = self.root)
                if Update>0:
                    conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "abhaytiwari@818" , database = "face_recognition" )
                    my_cursor = conn.cursor()
                    my_cursor.execute("update students set  name=%s , dep=%s , course= %s , year=%s , sem=%s , phone=%s , email=%s , gen=%s , dob=%s , radyn=%s where enroll=%s" ,  (
                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_gen.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_radyn.get(),
                                                                                                                                                                                        self.var_enroll.get()
                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success" , "Student Detsild successfully Updated" , parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error" , f"Due to : {str(es)}" , parent=self.root)
                
                
                
    #Function to delete data from database
    
    def delete_data(self):
        if self.var_enroll.get()=="":
            messagebox.showerror("Error" , "Student Id must be required" , parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete Student Data" , "Do you want to delete this Students Data" , parent = self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "abhaytiwari@818" , database = "face_recognition" )
                    my_cursor = conn.cursor()
                    sql = "delete from students where enroll=%s"
                    val = (self.var_enroll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
      
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete" , "Successfully Deleted Students Details" , parent = self.root)
            except Exception as es:
                messagebox.showerror("Error" , f"Due to : {str(es)}" , parent=self.root)
      
      
    
    # Function to reset data from Database
    
    def reset_data(self):
        self.var_enroll.set("")
        self.var_name.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Session")
        self.var_sem.set("Select Semester")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_gen.set("Select Gender")
        self.var_dob.set("")
        self.var_radyn.set("")
        
        
    
#-----------------------------------Generate Dataset to Take Photo Sample------------------------------------
      
      
    def generate_dataset(self):
        if self.var_course.get()=="Select Course" or self.var_dep.get()=="Select Department" or self.var_year.get()=="Select Session" or self.var_sem.get()=="Select Semester" or self.var_enroll.get()=="" or self.var_name.get()=="" or self.var_gen.get()=="Select Gender" or self.var_dob.get()=="" or self.var_phone.get()=="" or self.var_email.get()=="" :
            messagebox.showerror("Error" , "All Fields are Required" , parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "abhaytiwari@818" , database = "face_recognition" )
                my_cursor = conn.cursor()
                
                #to select everything from student table and put that into my_result variable
                my_cursor.execute("select * from students")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursor.execute("update students set  name=%s , dep=%s , course= %s , year=%s , sem=%s , phone=%s , email=%s , gen=%s , dob=%s , radyn=%s where enroll=%s" ,  (
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_radyn.get(),
                                                                                                                                                                                    self.var_enroll.get()==id+1  #used to give unique enroll.id to every pic clicked  
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # Load Predefined Data on FaceFrontal on OpenCV
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    grey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)  #the photos are converted to grey color i.e B/W
                    faces = face_classifier.detectMultiScale(grey , 1.3 , 5)
                    # Scaling Factor = 1.3
                    # Minimum Neighbour = 5
                    
                    #to crop the photo into passport size
                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                
                #to open web camera in system to click sample photo   
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret , my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame) , (450,450))  #resizing the cicked photos
                        face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user."+str(id)+"."+str(img_id)+".jpg"  #alloting inique id to every clicked photo
                        cv2.imwrite(file_name_path , face)
                        cv2.putText(face , str(img_id) , (50,50) , cv2.FONT_HERSHEY_COMPLEX , 2 , (0,255,0) , 2)  #font , font scale , color , thickness
                        cv2.imshow("Cropped Face" , face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==50:  #to capture number of pictures
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result" , "Generating data sets Completed!!!")
            except Exception as es:
                messagebox.showerror("Error" , f"Due to : {str(es)}" , parent=self.root)
      
      
      
      
      
# ----------------------------------------MAIN Function-------------------------------------------
      
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student_Details(root)
    root.mainloop()