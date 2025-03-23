from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata = []
class Attendance:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1280x690+0+0")
                self.root.title("Face Recognition System")
                
                #----------------------------Variables-------------------------------
                
                # self.var_attend_id = StringVar()
                self.var_attend_name = StringVar()
                self.var_attend_time = StringVar()
                self.var_attend_enroll = StringVar()
                self.var_attend_department = StringVar()
                self.var_attend_date = StringVar()
                self.var_attend_stat = StringVar()
                
                
                #-------------------------------GUI for Attendance--------------------------------
                
                
                #Frame for face recognition system label
                frs_frame = Frame(self.root , bg = "#01454c" )
                frs_frame.place(x=0 , y=0 , width=1280 , height=100)
                
                #Label for face recognition system 
                frs_label = Label(frs_frame , text="ATTENDANCE MANAGEMENT SYSTEM" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
                frs_label.place(x=10 , y=10 , width=1260 , height=80  )
                
                
                #Frame for main body
                main_frame = Frame(self.root , bg = "#01454c")
                main_frame.place(x=0 , y=100 , width=1280 , height=600)
                
                #Sub frame
                sub_frame = Frame(main_frame , bg = "#04163a")
                sub_frame.place(x=10 , y=10 , width=1260 , height=580)



                        #--------------------------------LEFT FRAME LABEL-----------------------------------------

                lft_lblf = LabelFrame(sub_frame , text = "Student Attendance Details", bd=4 , bg="#04163a" , fg="White" , font =( "Californian FB" , 20 , "bold"))
                lft_lblf.place(x=10,y=10,width = 620 , height = 500)


                # #Attendance ID
                # id_lbl = Label(lft_lblf , text="Attendance_Id" , fg="White" , bg="#04163a")
                # id_lbl.grid(row=0 , column=0 , padx=10 , pady=10)

                # id_ent = Entry(lft_lblf , width=25 , textvariable=self.var_attend_id)
                # id_ent.grid(row=0 , column=1 , padx=10 , pady=10)

                #Name
                name_lbl = Label(lft_lblf , text = "Name" , fg = "white" , bg = "#04163a")
                name_lbl.grid(row=0 , column=0 , padx=10 , pady = 10 )

                name_ent = Entry(lft_lblf , width=25 , textvariable=self.var_attend_name)
                name_ent.grid(row=0 , column=1 , padx=10 , pady=10)

                #Time
                time_lbl = Label(lft_lblf , text = "Time" , fg = "white" , bg = "#04163a")
                time_lbl.grid(row=1 , column=0 , padx=10 , pady = 10 )

                time_ent = Entry(lft_lblf , width=25 , textvariable=self.var_attend_time)
                time_ent.grid(row=1 , column=1 , padx=10 , pady=10)

                #Enroll No
                Enroll_lbl = Label(lft_lblf , text = "Enroll" , fg = "white" , bg = "#04163a")
                Enroll_lbl.grid(row=0 , column=3 , padx=10 , pady = 10 )

                Enroll_ent = Entry(lft_lblf , width=25 , textvariable=self.var_attend_enroll)
                Enroll_ent.grid(row=0 , column=4 , padx=10 , pady=10)

                #Department
                dept_lbl = Label(lft_lblf , text = "Department" , fg = "white" , bg = "#04163a")
                dept_lbl.grid(row=1 , column=3 , padx=10 , pady = 10 )

                dept_ent = Entry(lft_lblf , width=25 , textvariable=self.var_attend_department)
                dept_ent.grid(row=1 , column=4 , padx=10 , pady=10)


                #Date
                date_lbl = Label(lft_lblf , text = "Date" , fg = "white" , bg = "#04163a")
                date_lbl.grid(row=2 , column=3 , padx=10 , pady = 10 )

                date_ent = Entry(lft_lblf , width=25 , textvariable=self.var_attend_date)
                date_ent.grid(row=2 , column=4 , padx=10 , pady=10)

                #Attendance Status
                stat_lbl = Label(lft_lblf , text = "Attendance Status" , fg = "white" , bg = "#04163a")
                stat_lbl.grid(row=2 , column=0 , padx=10 , pady = 10 )

                stat_box = ttk.Combobox(lft_lblf , width=22 , textvariable=self.var_attend_stat)
                stat_box["values"] = ("Status" , "Present" , "Absent")
                stat_box.current(0)
                stat_box.grid(row=2 , column=1, padx=10 , pady=10)


        #----------------------------------------Frame for Buttons------------------------------------------------

                bttn_frm = Frame(lft_lblf , bg = "#04163a")
                bttn_frm.place(x=10 , y=340 , width=590 , height=80)


                #Import cvv
                imp_btt = Button(bttn_frm , text="Import CVV" , command=self.importCsv , width=35 )
                imp_btt.grid(row=0 , column=0 , padx=10 , pady=2)


                #Export cvv
                exp_btt = Button(bttn_frm , text="Export CVV" , command = self.exportCsv , width=35)
                exp_btt.grid(row=0, column=1 , padx=10 , pady=2)


                #Save
                save_btt = Button(bttn_frm , text="Save" , width=35)
                save_btt.grid(row=5 , column=0 , padx=20 , pady=5)


                #Reset
                reset_btt = Button(bttn_frm , command = self.reset_data , text="Reset" , width=35)
                reset_btt.grid(row=5 , column=1 , padx=20 , pady=5)


                #-------------------------------------Right Label Frame------------------------------------------

                ryt_lblf = LabelFrame(sub_frame , text = "Attendance Details", bd=4 , bg="#04163a" , fg="White" , font =( "Californian FB" , 20 , "bold"))
                ryt_lblf.place(x=640,y=10,width = 620 , height = 500)

                # table_frm = Frame(ryt_lblf , bg = "#04163a")
                # table_frm.place(x=5 , y=5 , width=620 , height=440)


                table_frame = Frame(ryt_lblf,bd=2 ,relief=RIDGE, bg = "#04163a")   
                table_frame.place(x=13,y=5,width=590,height=450)     

        # #----------------------------------------SCROLL BAR------------------------------------------------

                scroll_x = ttk.Scrollbar(table_frame , orient=HORIZONTAL)
                scroll_y = ttk.Scrollbar(table_frame , orient=VERTICAL)

                self.AttendanceReportTable=ttk.Treeview(table_frame,column=("enroll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.AttendanceReportTable.xview)
                scroll_y.config(command=self.AttendanceReportTable.yview)

                # self.AttendanceReportTable.heading("id",text="Attendance ID")
                self.AttendanceReportTable.heading("enroll",text="Enrollment No")
                self.AttendanceReportTable.heading("name",text="Name")
                self.AttendanceReportTable.heading("department",text="Department")
                self.AttendanceReportTable.heading("time",text="Time")
                self.AttendanceReportTable.heading("date",text="Date")
                self.AttendanceReportTable.heading("attendance",text="Attendance")
                self.AttendanceReportTable["show"]="headings"


                # self.AttendanceReportTable.column("id",width=100)
                self.AttendanceReportTable.column("enroll",width=100)
                self.AttendanceReportTable.column("name",width=100)
                self.AttendanceReportTable.column("department",width=100)
                self.AttendanceReportTable.column("time",width=100)
                self.AttendanceReportTable.column("date",width=100)
                self.AttendanceReportTable.column("attendance",width=100)

                self.AttendanceReportTable.pack(fill=BOTH,expand=1)
                self.AttendanceReportTable.bind("<ButtonRelease>" , self.get_cursor)
                
                
        
#----------------------------------------Functions------------------------------------------------       


        def fetchData(self , rows):
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in rows:
                        self.AttendanceReportTable.insert("" , END , values = i)
             
             
        #Import CSV
                
        def importCsv(self):
                global mydata
                mydata.clear()
                fln = filedialog.askopenfilename(initialdir = os.getcwd() , title="Open CSV" , filetypes=(("CSV File" , "*.csv") , ("All File" , "*.*")) ,  parent=self.root)
                with open(fln) as myfile:
                        csvread = csv.reader(myfile , delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchData(mydata)


        #Export CSV
        
        def exportCsv(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data" , "No Data Found to Export" , parent = self.root)
                                return False
                        fln = filedialog.asksaveasfilename(initialdir = os.getcwd() , title="Open CSV" , filetypes=(("CSV File" , "*.csv") , ("All File" , "*.*")) ,  parent=self.root)
                        with open(fln , mode="w" , newline="") as myfile:
                                exp_write = csv.writer(myfile , delimiter = ",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export" , "Your Data Exported to" +os.path.basename(fln)+"Successfully")
                except Exception as es:
                        messagebox.showerror("Error" , f"Due To :{str(es)}" , parent = self.root)
                
        
        # Get Data from File
        
        def get_cursor(self , event = ""):
                cursor_row = self.AttendanceReportTable.focus()
                content = self.AttendanceReportTable.item(cursor_row)
                rows = content['values']
                # self.var_attend_id.set(rows[0])
                self.var_attend_enroll.set(rows[0])
                self.var_attend_name.set(rows[1])
                self.var_attend_department.set(rows[2])
                self.var_attend_time.set(rows[3])
                self.var_attend_date.set(rows[4])
                self.var_attend_stat.set(rows[5])
                
        
        #Reset Data 
        def reset_data(self):
                self.var_attend_enroll.set("")
                self.var_attend_name.set("")
                self.var_attend_department.set("")
                self.var_attend_time.set("")
                self.var_attend_date.set("")
                self.var_attend_stat.set("")
        

        
if __name__ == "__main__":
        root = Tk()
        obj = Attendance(root)
        root.mainloop()