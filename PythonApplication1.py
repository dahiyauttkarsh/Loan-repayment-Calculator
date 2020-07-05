import tkinter as tk
from tkinter import ttk, font


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Loan Calculator")


amount_value = tk.DoubleVar()
interest_rate_value = tk.DoubleVar()
time_value = tk.DoubleVar()


cols = ("Month","Principal Amount","Payment Amount","Interest Amount","outstanding Balamce")
display = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    display.heading(col, text=col)
  




#-----calculation part

def Calculate(*args):
       
            amount=float(amount_value.get())
            y_rate=float(interest_rate_value.get())
            rate=y_rate/1200
            time=int(time_value.get())
            if amount>0 and rate>0 and time>0:
             for n in range(1,time+1):
             
                payment_amount =  ((rate * amount) * (1 + rate)**time) / (((1 + rate)**time) - 1)
         
                principal_amount = payment_amount/((1+rate)**(1+time-n))
         
                interest_amount = payment_amount - principal_amount
            
                out_bal = (interest_amount/rate) - principal_amount
                
                display.insert("","end",values=(n,round(payment_amount,2),round(principal_amount,2),round(interest_amount,2),round(out_bal,2)))

            else:
                display.insert("","end",values=("Error!!"))
               
def Del_data():
           
           amount_entry.delete(0,"end")
           interest_rate_entry.delete(0,"end")
           time_entry.delete(0,"end")
           display.delete(*display.get_children())

#- widgets

amount_label = tk.Label(root,text="Amount: ",fg="blue",bg="white")
amount_entry = ttk.Entry(root,textvariable=amount_value)
interest_rate_label = tk.Label(root,text="Interest Rate: ",fg="blue",bg="white")
interest_rate_entry = ttk.Entry(root,textvariable=interest_rate_value)
time_label = tk.Label(root,text="Enter the number of months: ",fg="blue",bg="white")
time_entry = ttk.Entry(root,textvariable=time_value)

amount_entry.delete(0,"end")
interest_rate_entry.delete(0,"end")
time_entry.delete(0,"end")


#- buttons
cal_button = ttk.Button(root,text="Calculate",command=Calculate)

del_button = ttk.Button(root,text="Clear",command=Del_data)

#- layout
amount_label.grid(row=0, column=0,columnspan=1, rowspan=1,sticky="n",padx=5)
amount_entry.grid(row=0, column=1,columnspan=1, rowspan=1,sticky="ew",padx=10)
interest_rate_label.grid(row=2, column=0,columnspan=1, rowspan=1,sticky="n",padx=5)
interest_rate_entry.grid(row=2, column=1,columnspan=1, rowspan=1,sticky="ew",padx=10)
time_label.grid(row=3, column=0,columnspan=1, rowspan=1,sticky="n",padx=5)
time_entry.grid(row=3, column=1,columnspan=1, rowspan=1,sticky="ew",padx=10)

cal_button.grid(row=4,sticky="n", column=1)
del_button.grid(row=5,column=1,sticky="n")

labelFont = font.Font(family='Helvetica', size=15, weight='bold')
label = tk.Label(root, text="Loan Payments", font=labelFont).grid(row=6,column=0,sticky="ew",columnspan=2)
display.grid(row=7,columnspan=2)
text_scroll = ttk.Scrollbar(root, orient="vertical", command=display.yview)
text_scroll.grid(row=7, column=2, sticky="ns")
display['yscrollcommand'] = text_scroll.set









#- shortcut key
root.bind("<Return>",Calculate)
root.bind("<BackSpace>",Del_data)


root.mainloop()
