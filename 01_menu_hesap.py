
from tkinter import*

pencere = Tk()

pencere.title("YEMEK HESAP SİSTEMİ")
pencere.geometry("650x600")
pencere.resizable(FALSE,FALSE)
pencere.configure(bg="light blue")


def Tutar():
    s1 = str(entPizza.get())
    if s1.isdigit():
        s1 = int(entPizza.get())
    else:
        s1 = 0

    s2 = str(entCola.get())
    if s2.isdigit():
        s2 = int(entCola.get())
    else:
        s2 = 0

    s3=str(entSutlac.get())
    if s3.isdigit():
        s3 = int(entSutlac.get())
    else:
        s3 = 0

    lblToplamTutar['text'] = str(s1*25 + s2*3 + s3*5) + str(" TL")


def Temizle():
    entPizza.delete(0,"end")
    entCola.delete(0, "end")
    entSutlac.delete(0, "end")
    lblToplamTutar['text'] =""


lblBaslik = Label(pencere, text="Yemek Hesap Sistemi", font="Verdana 20 bold", bg="light blue")
lblBaslik.place(x=160,y=10)

lblYiyecekler = Label(pencere, text="YİYECEKLER", font="Verdana 14 bold", bg="green")
lblYiyecekler.place(x=50, y=70)

lblPizza = Label(pencere, text="Pizza(25 TL)", font="Verdana 12 bold", bg="light blue")
lblPizza.place(x=30, y=130)

lblicecekler = Label(pencere, text="İÇECEKLER", font="Verdana 14 bold", bg="green")
lblicecekler.place(x=250, y=70)

lblCola = Label(pencere, text="Cola (3 TL)", font="Verdana 12 bold", bg="light blue")
lblCola.place(x=250, y=130)

lblTatlilar = Label(pencere, text="TATLILAR", font="Verdana 14 bold", bg="green")
lblTatlilar.place(x=460, y=70)

lblSutlac = Label(pencere, text="Sütlaç (5 TL)", font="Verdana 12 bold", bg="light blue")
lblSutlac.place(x=450, y=130)

lblToplamTutar = Label(pencere, text="", font="Verdana 14 bold", width=20, height=1, bg="light blue")
lblToplamTutar.place(x=170, y=460)

entPizza = Entry(pencere, font="Verdana 12 bold")
entPizza.place(x=30, y=170, width=150)

entCola = Entry(pencere, font="Verdana 12 bold")
entCola.place(x=240, y=170, width=150)

entSutlac = Entry(pencere, font="Verdana 12 bold")
entSutlac.place(x=450, y=170, width=150)

btnToplamTutar = Button(pencere, text="TOPLAM TUTAR", font="Verdana 16 bold", command=Tutar)
btnToplamTutar.place(x=210, y=400)

btnTemizle = Button(pencere, text="TEMİZLE", font="Verdana 16 bold", command=Temizle)
btnTemizle.place(x=250, y=520)


pencere.mainloop()

