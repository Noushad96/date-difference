#########   Date calculator        ##############
from tkinter import *     # import all methods and classes from the tkinter
#tkcalendar module install bhi krna hoga
from tkcalendar import DateEntry   # import DateEntry from tkcalen

root=Tk()
root.geometry("300x200")
root.title("Date calculator")

def difference():
    date_dif=cal1.get_date() - cal2.get_date() #date difference
    combo1.set(date_dif) # date_dif ka value combo1 me update kr do


lbl=Label(root,text="Date difference",font="arial 15 bold").grid(row=1,column=2)

################# from #############
lbl=Label(root,text="From",font="arial 15 bold").grid(row=2,column=1)
cal1 = DateEntry(root, width=10, year=2020, month=6, day=2,font="arial 15 bold", background='darkblue', foreground='white', borderwidth=2)
cal1.grid(row=2,column=2)

############## To ###############

lbl=Label(root,text="To",font="arial 15 bold").grid(row=3,column=1)
cal2 = DateEntry(root, width=10, year=2019, month=6, day=22,font="arial 15 bold", background='darkblue', foreground='white', borderwidth=2)
cal2.grid(row=3,column=2)


############ Difference #############

lbl3=Label(root,text="Differnce",font="arial 15 bold").grid(row=5,column=1)
b=Button(root,text="click",font="lucinda 15 bold",command=difference).grid(row=4,column=2)

combo1=StringVar(root)
entry1=Entry(root,textvariable=combo1,font="arial 12 bold",width=18).grid(row=5,column=2)

root.resizable(0,0)  # frame ko fix kr diya
root.mainloop()
