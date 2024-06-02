import pytube
from tkinter import * 
from tkinter import messagebox
import os 

def download_video():
    video_url = entry_url.get()
    path = os.path.join(os.environ['USERPROFILE'], 'Desktop')

    try:
        yt = pytube.YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(path)
        status_label.config(text="Video başarıyla indirildi!", fg="green")
    except Exception as e:
        status_label.config(text=f'Hata oluştu: {e}', fg="red")

# Tkinter Pencere
wd = Tk()
wd.title("Yt Video Downloader")
wd.config(padx=30,pady=30)

# Url Giris etiketi
url_label = Label(wd, text="Enter video URL:")
url_label.pack()

# url Giris
entry_url = Entry(width=30)
entry_url.pack()

# Dow Button
dow_btn = Button(wd, text="Download",command=download_video)
dow_btn.pack()

# Durum etiketi
status_label = Label(wd, text="", fg="red")
status_label.pack()

wd.mainloop()


