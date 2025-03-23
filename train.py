from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import numpy as np
import mysql.connector
import os
import cv2


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x690+0+0")
        self.root.title("Face Recognition System")
        
        #Frame for face recognition system label
        frs_frame = Frame(self.root , bg = "#01454c" )
        frs_frame.place(x=0 , y=0 , width=1280 , height=100)
        
        #Label for face recognition system 
        frs_label = Label(frs_frame , text="FACE RECOGNITION ATTENDANCE SYSTEM" , fg = "White" , bg = "#015b66" , font=("Latin" , 30 , "bold"))
        frs_label.place(x=10 , y=10 , width=1260 , height=80  )
        
        
        #Frame for main body
        main_frame = Frame(self.root , bg = "#01454c")
        main_frame.place(x=0 , y=100 , width=1280 , height=600)
        
        #Sub frame
        sub_frame = Frame(main_frame , bg = "#04163a")
        sub_frame.place(x=10 , y=10 , width=1260 , height=570)
        
        
        #----------------------------------------------------------
        
        img1 = Image.open(r"C:\VS Code\Face Recognition Attendance System Project\photos\train.png")
        img1 = img1.resize((250,250))
        self.photoimg1 = ImageTk.PhotoImage(img1)
         
        img_lbl =Label(sub_frame , image=self.photoimg1 )
        img_lbl.place(x=500 , y= 150 , width=250 , height=250)        
        
        #BUTTON
        bt=Button(sub_frame,text="Train Data", command=self.train_classifier , cursor="hand2",font=("timer new roman",20),bg="white",fg="black")
        bt.place(x=500,y=405,width=251,height=40)
        
        
#-----------------------------------------Functions to Train Data --------------------------------------
        
        
    def  train_classifier(self):  
        data_direct=("Data") 
        path=[os.path.join(data_direct,file) for file in os.listdir(data_direct)] 
        
        #created 2 empty list to store faces and id's
        faces=[] 
        ids=[] 
        
        for image in path: 
            img=Image.open(image).convert('L')   #convert the images into grey scale image
            imageNp=np.array(img,'uint8')   #uint8 is a data type
            id=int(os.path.split(image)[1].split('.')[1]) 
    
            #append/stores the emages and id's in list
            faces.append(imageNp) 
            ids.append(id) 
            cv2.imshow("Traning data",imageNp)
            cv2.waitKey(1) == 13
            
        #used numpy to convert into array  
        ids=np.array(ids) 
        
        
    #============== Train the classifier and save================# 
    
        #used LBPH : Local Binary Pattern Histogram
        clf=cv2.face.LBPHFaceRecognizer_create() 
        clf.train(faces,ids)   #trained the data
        clf.write("classifier.xml")   #created an xml file to store the data
        
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Traning Datasets Completed" , parent=self.root)

        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()