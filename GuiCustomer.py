from Shop import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


def see_store():
    messagebox.showinfo(f'"{s.name}" in {s.city}',s)

def checkout():
    price=s.calculate_rental_price(var.get(),
                             amount_of_time.get(), s.find_by_company(combo2.get()),False,combo.get())
    if price!=False:
        answer=messagebox.askyesno("Price",f"It will cost {price}$.\nMy friend")
        if answer==True:
            price = s.calculate_rental_price(var.get(),
                                         amount_of_time.get(), s.find_by_company(combo2.get()),answer, combo.get())
            messagebox.showinfo("Rented New Bikes",f"Thanks\n You have just paid {price}$")
            print(f"sold {combo2.get()}, inventory: {s.bikes[s.find_by_company(combo2.get())]}")
    else:
        bike=s.find_by_company(combo2.get())
        messagebox.showerror("There are not Available Bikes", f"We have just {s.bikes[bike]} bikes of {bike.company} ")

win=Tk()
win.geometry('470x350')
win.title('Bikes Rental')

title=Label(win,text='Bike Rental',font=('David',26))
title.grid(row=0, column=0)

title2=Label(win,text='Choose your plan:',font=('David',14))
title2.grid(row=1, column=0)

var=StringVar()
rad_day = Radiobutton(win,text='Daily',value="daily",variable=var)
rad_hour = Radiobutton(win,text='Hourly',value="hourly",variable=var)
rad_week = Radiobutton(win,text='Weekly',value="weekly",variable=var)
rad_day.grid(row=3,column=0)
rad_hour.grid(row=2,column=0)
rad_week.grid(row=4,column=0)

title3=Label(win,text='How many hours/days/weeks?',font=('David',14))
title3.grid(row=5, column=0)

amount_of_time=Combobox(win, values=[i for i in range(1, 12)])
amount_of_time.grid(row=6, column=0)
amount_of_time.current(0)

title3=Label(win,text='How many bikes would you like my friend?',font=('David B',14))
title3.grid(row=7,column=0)



combo=Combobox(win,values=[1,2,3,4,5])
combo.grid(row=8,column=0)
combo.current(0)



combo2=Combobox(win,values=s.get_bikes_company())
combo2.grid(row=9,column=0)
combo2.current(0)

button= Button(win,text='Check Me Out',command=checkout)
button.grid(row=10,column=0)

see_store=Button(win,text='See Available Bikes',command=see_store)
see_store.grid(row=1,column=1)

win.mainloop()