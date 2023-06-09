import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
# ایجاد کردن فرم
root = Tk()
root.title("ادیتور سعید انتظاری")
root.configure(bg="Teal")
Label(root, text="name pic1 with format").grid(row=0, column=0)
Label(root, text="name pic2 with format",fg="blue").grid(row=1, column=0)
Label(root, text="Made by Saeed_Entezari_maleki❤👨‍💻").grid(row=0, column=5)

e1=Entry(root,fg='black')
e2=Entry(root,fg='blue')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def gray():
    img=cv2.imread(e1.get())
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
def open_pic():
    img=cv2.imread(e1.get())
    print(img)
    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
def matrisi():
    img=np.zeros([800,800])
    print(img)
    cv2.imwrite(e1.get(),img)
    cv2.waitKey()
    cv2.destroyAllWindows()  
def siyah_be_sefid():
    img=cv2.imread(e1.get(),0)
    kernel=np.ones((5,5),np.uint8)
    gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
    cv2.imshow("img",img)
    cv2.imshow("gradient",gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize():
    img1=cv2.imread(e1.get())
    img2=cv2.imread(e2.get())
    cv2.imshow('first img 1.get()',img1)
    cv2.imshow('first img e2.get()',img2)
    width=img1.shape[1]
    height=img1.shape[0]
    img2=cv2.resize(img2,(width,height))
    cv2.imshow('resize img',img2)

def blend():
    img1=cv2.imread(e1.get())
    img2=cv2.imread(e2.get())
    width=img1.shape[1]
    height=img1.shape[0]
    img2=cv2.resize(img2,(width,height))
    blend=cv2.addWeighted(img1,1.1,img2,1.6,3)
    cv2.imwrite("belnd.jpg",blend)
    cv2.imshow("belnd.jpg",blend)
def teyfe_rangi():
    img=cv2.imread(e1.get(),1)
    cv2.imshow('img',img)
    histogram=cv2.calcHist([img],[0],None,[256],[0,255])#image chanal mask size range
    hist=plt.plot(histogram)
    plt.show()
def hist_khat():
    img=cv2.imread(e1.get(),cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image',img)
    plt.imshow(img,cmap='gray',interpolation='bicubic')
    hist=plt.plot([100,400],[200,300],'b',linewidth=10)
    plt.show()
def pic_khat_mostatil():
    img=cv2.imread(e1.get())
    cv2.imshow('image1',img)
    img=cv2.line(img,(200,300),(300,400),(255,255,255),6)
    img=cv2.rectangle(img,(200,300),(400,500),(0,120,255),3)
    cv2.imshow('image2',img)
def pic_mosalas():
    img=cv2.imread(e1.get())
    cv2.imshow('image1',img)
    pts=np.array([[50,100],[120,200],[250,100],[400,20]])
    img=cv2.polylines(img,[pts],False,(60,40,25),3)
    cv2.imshow('image2',img)
def etelaat_satr_pic():
    img=cv2.imread(e1.get(),cv2.IMREAD_COLOR)
    px=img[200,200]
    print(px)
def moraba_roye_pic():
    img=cv2.imread(e1.get(),cv2.IMREAD_COLOR)
    img[100:200,100:200]=[0,0,255]
    cv2.imshow('image',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
def edgham_pics():
    img1=cv2.imread(e1.get())
    img2=cv2.imread(e2.get())
    width=img1.shape[1]
    height=img1.shape[0]
    img3=cv2.resize(img2,(width,height))
    add=img1+img3
    cv2.imshow('image',add)
    cv2.waitKey()
    cv2.destroyAllWindows()
def logo ():
    img1=cv2.imread(e1.get())
    img2=cv2.imread(e2.get())
    cv2.imshow('src',img2)
    rows,cols,channels=img2.shape
    roi=img1[0:rows,0:cols]
    img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    cv2.imshow('src_gray',img2gray)
    ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY)
    cv2.imshow('mask',mask)
    mask_inv=cv2.bitwise_not(mask)
    cv2.imshow('mask_inv',mask_inv)
    img1_bg=cv2.bitwise_and(roi,roi,mask=mask)
    cv2.imshow('mask_bg',img1_bg)
    img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)
    cv2.imshow('mask_fg',img2_fg)
    dst=cv2.add(img1_bg,img2_fg)
    img1[0:rows,0:cols]=dst
    cv2.imshow('image',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def labeyabi():
    img=cv2.imread(e1.get())
    laplacian=cv2.Laplacian(img,cv2.CV_8U)
    cv2.imshow('original',img)
    cv2.imshow('laplacian',laplacian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def webcam_labeyabi():
    cap=cv2.VideoCapture(0)
    fg=cv2.createBackgroundSubtractorMOG2()
#cv2.imshow('fg',fg)
    while True:
        _,frame=cap.read()
        fmask=fg.apply(frame)
        cv2.imshow('original',frame)
        cv2.imshow('fg',fmask)
        k=cv2.waitKey(27) & 0xFF
        if (k==27):
         break
    cv2.destroyAllWindows()
    cap.release()
def webcam_tashkhis_chehre():
    faceXML=cv2.CascadeClassifier('haarcascade_eye.xml')
    eyeXML=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap=cv2.VideoCapture(0)
    while(True):
        _,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=faceXML.detectMultiScale(gray)

        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h , x:x+w]
            roi_color=frame[y:y+h , x:x+w]
            eyes=eyeXML.detectMultiScale(roi_gray)
            for(ex,ey,ew,eh) in eyes:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
  
        cv2.imshow('face',frame)
        k=cv2.waitKey(27)& 0XFF
        if (k==27):
          break
    cv2.destroyAllWindows()
def contrast_pic1():
    img=cv2.imread(e1.get())
    cv2.imshow("img",img)
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("img2",img2)
    cv2.waitKey(0)
Button(root, text='quit',command=root.quit,fg='red').grid(row=10, column=3)
Button(root, text="open", command=open_pic,fg="Brown").grid(row=2, column=2)
Button(root, text="matrisi", command=matrisi,fg='Black').grid(row=2, column=3)
Button(root, text="siyah_be_sefid", command=siyah_be_sefid,fg='green').grid(row=2, column=4)
Button(root, text="resize pic2", command=resize,fg='Brown').grid(row=3, column=2)
Button(root, text="teyfe_rangi", command=teyfe_rangi,fg='Black').grid(row=3, column=3)
Button(root, text="blend", command=blend,fg='green').grid(row=3, column=4)
Button(root, text="hist_khat", command=hist_khat,fg='Brown').grid(row=4, column=2)
Button(root, text="pic_khat_mostatil", command=pic_khat_mostatil,fg='Black').grid(row=4, column=3)
Button(root, text="pic_mosalas", command=pic_mosalas,fg='green').grid(row=4, column=4)
Button(root, text="etelaat_pic", command=etelaat_satr_pic,fg='Brown').grid(row=5, column=2)
Button(root, text="moraba_roye_pic", command=moraba_roye_pic,fg='Black').grid(row=5, column=3)
Button(root, text="edgham_pics", command=edgham_pics,fg='green').grid(row=5, column=4)
Button(root, text="gray", command=gray,fg='Brown').grid(row=6, column=2)
Button(root, text="logo roye aks", command=logo,fg='Black').grid(row=6, column=3)
Button(root, text="labeyabi logo", command=labeyabi,fg='Brown').grid(row=7, column=2)
Button(root, text="webcam_labeyabi", command=webcam_labeyabi,fg='Black').grid(row=7, column=3)
Button(root, text="webcam_tashkhis_chehre", command=webcam_tashkhis_chehre,fg='green').grid(row=7, column=4)
Button(root, text="contrast_pic1", command=contrast_pic1, fg='green').grid(row=6, column=4)
root.mainloop()