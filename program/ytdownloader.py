from pytube import YouTube
link = "https://youtu.be/8jsWDv7cvig"
yt= YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
print("vidio berhasil di download")





# from tkinter import *

# root = Tk()
# root.geometry('600x300')

# Label = Label(ro)