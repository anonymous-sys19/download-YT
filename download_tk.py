from tkinter import * 
import pytube  
root = Tk()  
root.geometry('600x400')    
root.title('youtube video downloader')  
Label(root, text = 'Youtube Video Downloader',  font ='arial 20 bold').pack()  
  
link = StringVar()  
path = StringVar()

Label(root,  text = 'Paste Youtube Link Here:',  font = 'arial 15 bold').place(x = 50,   y = 50)
link_enter = Entry(root,  width = 50, textvariable = link).place(x = 50,  y = 80)

Label(root,  text = 'Enter path to save:',  font = 'arial 15 bold').place(x = 50,   y = 110)  
path_enter = Entry(root,  width = 50, textvariable = path).place(x = 50,  y = 150)  
def Downloader():  
    url = pytube.YouTube(str(link.get()))  
    video = url.streams.get_highest_resolution()  
    video.download(str(path.get()))  
    Label(root,  text = ' VIDEO DOWNLOADED',  font = 'arial 15', bg='yellow').place(x= 180,   y = 240)  
Button(root, text = 'DOWNLOAD VIDEO',  font = 'arial 15 bold',  bg = 'cyan',  padx = 2,  command = Downloader).place(x=180,  y = 200)  
root.mainloop()
