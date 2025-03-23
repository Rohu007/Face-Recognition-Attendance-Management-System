from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        #Here we created the frame

        frs_frame = Frame(self.root , bg = "#01454c" )
        frs_frame.place(x=0 , y=0 , width=1280 , height=100)
        
        #Label for face recognition system 
        frs_label = Label(frs_frame , text="FACE RECOGNITION" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
        frs_label.place(x=10 , y=10 , width=1260 , height=80  )

        
        #Frame for main body
        main_frame = Frame(self.root , bg = "#01454c")
        main_frame.place(x=0 , y=100 , width=1280 , height=600)
        
        #Sub frame
        sub_frame = Frame(main_frame , bg = "#04163a")
        sub_frame.place(x=10 , y=10 , width=1260 , height=580)
        
        #Inserting an background image in the frame

        img=Image.open(r"C:\VS Code\Face Recognition Attendance System Project\photos\recog.png.jpg")
        img=img.resize((250,250))
        self.photo=ImageTk.PhotoImage(img)

#-----------------------------------------------------------------------------------------

        #Placing the image on the frame 

        f_lbl=Label(sub_frame,image=self.photo)
        f_lbl.place(x=510,y=100,width=250,height=250)

        #BUTTON
        bt=Button(sub_frame,text="Face Recognition" , command=self.Face_recog , cursor="hand2",font=("timer new roman",20),bg="white",fg="black")
        bt.place(x=510,y=355,width=251,height=40)


#------------------------------------------Face Recognition Function ---------------------------------------------
        
        
    def Face_recog(self):
        def Draw_boundary(img , classifier , scalefactor , MinNeighbors , color , test , clf):
            gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert image to gray
            Features = classifier.detectMultiScale(gray_img , scalefactor , MinNeighbors)

            coord=[] #to draw rectangle

            #to create rectangle square
        
            for(x , y , w , h) in Features:
                cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,255,0) , 3) #inbuilt function
                
                #img and id ko predict kr rhe h same h ki nai
                id , predict = clf.predict(gray_img[y:y+h,x:x+w]) #to predict img  #(y:y+h,x:x+w) giving position
                
                confidence=int((100*(1-predict/300))) #formula for prediciton 

                conn = mysql.connector.connect(host = "127.0.0.1" , username = "root" , password = "abhaytiwari@818" , database = "face_recognition" )
                my_cursor = conn.cursor()

        
                # Performing queries to fetch info
                #Info to be shown on top of square box 
                
                my_cursor.execute("select enroll from students where enroll ="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("select name from students where enroll ="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
        
                my_cursor.execute("select dep from students where enroll ="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence>77:  # shows probability of img being detect correctly
                            #setting img font color thickness etc
                    cv2.putText(img,f"Enroll:{r}" , (x,y-55) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , (255,255,255) , 3)
                    cv2.putText(img , f"Name:{n}" , (x,y-30) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , (255,255,255) , 3)
                    cv2.putText(img,f"Department:{d}" , (x,y-5) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , (255,255,255) , 3)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0) , 3)
                    cv2.putText(img , "Unknown Person" , (x,y-5) , cv2.FONT_HERSHEY_COMPLEX , 0.8 , (255,255,255) , 3)

                coord.append((x , y , w, h))  
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = Draw_boundary(img,faceCascade , 1.1 , 10 , (255,25,255) , "Face" , clf)
            return img
    
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") 
            #train data m write kiya tha ab is read kiya h 
            
            #To capture video and take img  front camera access ke liye 0 for other 1
        video_cap = cv2.VideoCapture(0)


        while True:
            ret,img = video_cap.read()
            if not ret:
                break
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recogntion",img) #webcam window title

            if cv2.waitKey(1) == 27: 
                #window open rhegi jb tk enter na dabaye means waitkey 1 h 
                break

        video_cap.release() #to close video file or capturing device
        cv2.destroyAllWindows()
    
    
    
    #------------------------------------Function For Marking Attendance-------------------------------------------
        
        
    def mark_attendance(self , r , n , d):
        with open("SAttendance.csv" , "r+" , newline="\n") as f:
            myDataList = f.readlines()
            enroll_list = []
            for line in myDataList:
                entry = line.split((","))
                enroll_list.append(entry[0])
            if(r not in enroll_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"{r},{n},{d},{dtstring},{d1},Present\n")
            
            
        
        
        
        
if  __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root) 
    root.protocol("WM_DELETE_WINDOW", obj.root.destroy)
    root.mainloop()
    
