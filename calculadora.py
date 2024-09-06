from tkinter import *
import pyautogui as pg
import time

def ReceberEntradas():
    a=entry1.get()
    b=int(entry2.get())
    x=0
    time.sleep(3)
    while x<b:
        pg.write(f"{a}, #{x+1}\n")
        x+=1

root = Tk()
root.geometry("350x700")
root.title("Enviador de texto")
root.config(bg="lightblue")

entry1=Entry(root)
entry1.place(relx=0.1,rely=0.05)
entry2=Entry(root)
entry2.place(relx=0.1,rely=0.1)
bnt=Button(root,bg="darkgreen",text="Enviar",command=ReceberEntradas,foreground="white")
bnt.place(relx=0.1,rely=0.15)



root.mainloop()