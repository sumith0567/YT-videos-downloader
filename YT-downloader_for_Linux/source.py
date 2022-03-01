from pytube import YouTube
import tkinter as tk

def down():
  a=i.get("1.0", "end-1c")
  YouTube(a).streams.get_highest_resolution().download("sr-downloads")

sr=tk.Tk()
sr.title("Download YT Videos : )")
sr.geometry("500x400")
sr.maxsize(500,400)
sr.minsize(500,400)
sr.configure(bg="#2288aa")

l=tk.Label(sr,text="Paste YT Link:",height=2,width=15,font=("italic",22),bg="#2288aa",fg="white").place(x=100,y=20)
i=tk.Text(sr,height=1,width=20,font=(None,20))

b=tk.Button(sr,text="Download",command=lambda:down(),height=2,width=15,font=("italic",20),bg="#00aa55",fg="#ffffff").place(x=120,y=200)
b2=tk.Button(sr,text="!",command=lambda:exit(),height=1,width=1,font=("oblique",20),bg="red",fg="#ffffff").place(x=425,y=200)

i.place(x=80,y=120)

l=tk.Label(sr,text="NOTE:\n*wait untill button turns green to complete download.\n*downloads will be saved in 'sr-downloads' folder.\n\tART BY :- SUMITH D",height=4,width=45,font=("italic",12),bg="#cc8899",fg="white").place(x=20,y=300)

sr.mainloop()