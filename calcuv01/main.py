from tkinter import *

eredmeny=""

root = Tk()
root.geometry("430x860")
root.configure(bg="black")

egyes = PhotoImage(file='jpgs/1.png')
kettes = PhotoImage(file='jpgs/2.png')
harmas = PhotoImage(file='jpgs/3.png')
negyes = PhotoImage(file='jpgs/4.png')
otos = PhotoImage(file='jpgs/5.png')
hatos = PhotoImage(file='jpgs/6.png')
hetes = PhotoImage(file='jpgs/7.png')
nyolcas = PhotoImage(file='jpgs/8.png')
kilences = PhotoImage(file='jpgs/9.png')
nullas = PhotoImage(file='jpgs/zero.png')

clear=PhotoImage(file="jpgs/clear.png")
dot=PhotoImage(file="jpgs/dot.png")
equal=PhotoImage(file="jpgs/equal.png")
osztas=PhotoImage(file="jpgs/in.png")
minplus=PhotoImage(file="jpgs/minplus.png")
perc=PhotoImage(file="jpgs/perc.png")
plus=PhotoImage(file="jpgs/plus.png")
minus=PhotoImage(file="jpgs/minus.png")
szorz=PhotoImage(file="jpgs/x.png")
x="alma"

#top
elszoszint=Label(bg="black").grid(row=0, column=0)
maosdikszint=Label(bg="black").grid(row=1, column=2)
eredmeny=Label(text=eredmeny,bg="black",fg="white").grid(row=2, column=0, columnspan=4)

#elsoszint
torles=Button(image=clear, bg="black", borderwidth=0,highlightthickness="10").grid(row=3, column=0, pady=0)
plusmin=Button(image=minplus, bg="black", borderwidth=0,highlightthickness="10").grid(row=3, column=1, pady=0)
percent=Button(image=perc, bg="black", borderwidth=0,highlightthickness="10").grid(row=3, column=2, pady=0)
oszt=Button(image=osztas, bg="black", borderwidth=0,highlightthickness="10").grid(row=3, column=3, pady=0)

#masodikszint
het=Button(image=hetes, bg="black", borderwidth=0,highlightthickness="10").grid(row=4, column=0, pady=0)
nyolc=Button(image=nyolcas, bg="black", borderwidth=0,highlightthickness="10").grid(row=4, column=1, pady=0)
kilenc=Button(image=kilences, bg="black", borderwidth=0,highlightthickness="10").grid(row=4, column=2, pady=0)
szorzas=Button(image=szorz, bg="black", borderwidth=0,highlightthickness="10").grid(row=4, column=3, pady=0)

#harmadikszint
negy=Button(image=negyes, bg="black", borderwidth=0,highlightthickness="10").grid(row=5, column=0, pady=0)
ot=Button(image=otos, bg="black", borderwidth=0,highlightthickness="10").grid(row=5, column=1, pady=0)
hat=Button(image=hatos, bg="black", borderwidth=0,highlightthickness="10").grid(row=5, column=2, pady=0)
minusz=Button(image=minus, bg="black", borderwidth=0,highlightthickness="10").grid(row=5, column=3, pady=0)

#negyedikszint
egy=Button(image=egyes, bg="black", borderwidth=0,highlightthickness="10").grid(row=6, column=0, pady=0)
ketto=Button(image=kettes, bg="black", borderwidth=0,highlightthickness="10").grid(row=6, column=1, pady=0)
harom=Button(image=harmas, bg="black", borderwidth=0,highlightthickness="10").grid(row=6, column=2, pady=0)
plusz=Button(image=plus, bg="black", borderwidth=0,highlightthickness="10").grid(row=6, column=3, pady=0)

#otodikszint
zero=Button(image=nullas, bg="black", borderwidth=0,highlightthickness="10").grid(row=7, column=0,columnspan=2, pady=0)
pont=Button(image=dot, bg="black", borderwidth=0,highlightthickness="10").grid(row=7, column=2, pady=0)
egyen=Button(image=equal, bg="black", borderwidth=0,highlightthickness="10").grid(row=7, column=3 , pady=0)

szamok=[320,32]
cmnds=["/"]
szamokhossz=len(szamok)
szamh=1
y=0
while 0==0:
    print(szamok)
    if cmnds[y]=="-":
        szam1=szamok[0]
        szam2=szamok[szamh]

        eredmeny=szam1-szam2
        szamok[0]=eredmeny

    elif cmnds[y] == "/":
        szam1 = szamok[0]
        szam2 = szamok[szamh]

        eredmeny = szam1/szam2
        szamok[0] = eredmeny

    elif cmnds[y] == "x":
        szam1 = szamok[0]
        szam2 = szamok[szamh]

        eredmeny = szam1*szam2
        szamok[0] = eredmeny

    elif cmnds[y] == "+":
        szam1 = szamok[0]
        szam2 = szamok[szamh]

        eredmeny = szam1+szam2
        szamok[0] = eredmeny
    szamh+=1
    if y==len(cmnds)-1:
        break
    print(y)
    y+=1


root.mainloop()
