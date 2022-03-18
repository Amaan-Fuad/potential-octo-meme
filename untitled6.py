from tkinter import*
import random
amaan=Tk()
amaan.geometry("600x400")
amaan.title("Random Colors")

dictionary1={"Colors":["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def random_colors():
    rc=random.randint(0,7)
    print(dictionary1["Colors"][rc])
    amaan.configure(background=dictionary1["Colors"][rc])
button1=Button(amaan,text="Click me",command=random_colors)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)
amaan.mainloop()