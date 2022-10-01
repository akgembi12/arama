from tkinter import *
import webbrowser as wb



def Ara(r):
    kelime=giris.get()
    url="https://www.google.com/search?q="+kelime
    wb.open(url)


pencere=Tk()
pencere.title("Google Arama")
pencere.geometry("900x500")
pencere.configure(background="white")

ikon=PhotoImage(file="ara.png")
gikon=PhotoImage(file="google.png")


giris=Entry(pencere)
giris.config(font=("Arial",30),bd=50)
giris.place(x=158,y=152)


btn=Button(pencere, image=ikon)
btn.config(text="Ara",font=("Arial",25),command=Ara,bd=2)
btn.place(x=650,y=200)

giris.bind_all("<Return>",Ara)

resim=Label(pencere,image=gikon,bd=0)
resim.place(y=10,x=300)

pencere.mainloop()
