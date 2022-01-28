# YouTube Video Downloader by @code-today
from tkinter import *
from tkinter.font import BOLD
from pytube import YouTube

root = Tk()
root.geometry('300x400')
root.resizable(0,0)
# background img
bg = PhotoImage(file='background.png')
blabel = Label(root,image=bg)
blabel.place(x=0,y=0)
#title
root.title("Youtube video downloader - by arpit")
#labels
Label(root, text ='YouTube Downloader', font ='arial 20 bold',fg="white",bg='black',pady=10).pack()
Label(root, text ='<< select quality >>', font ='arial 10 bold',fg="white",bg='black',pady=15).pack()
#logo
logo = PhotoImage(file='logo1.png')
logolabel = Label(root,image=logo)
logolabel.configure(borderwidth=0)
logolabel.place(x=125,y=45)
#link
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold',fg="white",bg='black').place(x= 65 , y = 195)
#link taking
link = StringVar()
link_enter = Entry(root, width = 45,textvariable = link).place(x = 12, y = 235)


#radio button of quality selection

var = IntVar()
var.set(1)
def set():
    print("selection: ",var.get())
    global selection
    selection = str(var.get())

Radiobutton(root, text = '360p', variable = var,
                value = '18', indicator = 0,background = "white",selectcolor="red",command=set).pack(fill = X, ipady = 1)
Radiobutton(root, text = '720p', variable = var,
                value = '22', indicator = 0,background = "white",selectcolor="red",command=set).pack(fill = X, ipady = 1)
Radiobutton(root, text = '1080p', variable = var,
                value = '137', indicator = 0,background = "white",selectcolor="red",command=set).pack(fill = X, ipady = 1)


#Functions
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.get_by_itag(selection)
    video.download()
    Label(root, text = 'Video Downloded!', font = 'arial 15',fg="white",bg = 'black').place(x= 65 , y = 320)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'black',fg='red', padx = 2, command = Downloader).place(x=80 ,y = 270)
# develop by
Label(root, text = '           || Developed by - Arpit Pathak ||', font = 'arial 10',fg="white",bg="#bf0000").place(x= 15 , y = 370) 
root.mainloop()
