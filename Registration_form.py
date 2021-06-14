from tkinter import * 
import tkinter.messagebox
root=Tk()
root.title("Employee Details Registration form")
root.configure(backgrou="grey")

label1=Label(root,text="Employee Registration Form",font=("bold",20),bg="grey").grid(row=0,column=1,columnspan=5)
first_name=Label(root,text="First name",font=("bold",12),bg="grey").grid(row=1,column=1)
last_name=Label(root,text="Last name",font=("bold",12),bg="grey").grid(row=2,column=1)
emp_id=Label(root,text="Employee ID",font=("bold",12),bg="grey").grid(row=3,column=1)
#creating dropdown list
dept=['IT','HR','Marketing','Production']
d=StringVar()
droplist=OptionMenu(root,d,*dept)
droplist.config(width=15)
d.set('your Department')
droplist.grid(row=4,column=2,ipadx=100)
Department=Label(root,text="Depatment",font=("bold",12),bg="grey").grid(row=4,column=1)
email=Label(root,text="Email ID",font=("bold",12),bg="grey").grid(row=5,column=1)
Phone_no=Label(root,text="Phone no",font=("bold",12),bg="grey").grid(row=6,column=1)
#creating radiobuttons
gen=IntVar()
Radiobutton(root,text="Male",padx=35,variable=gen,value=1,width=20).grid(row=7,column=2)
Radiobutton(root,text="Female",padx=35,variable=gen,value=2,width=20).grid(row=7,column=3)
Gender=Label(root,text="Gender",font=("bold",12),bg="grey").grid(row=7,column=1)
City=Label(root,text="City",font=("bold",12),bg="grey").grid(row=8,column=1)
State=Label(root,text="State",font=("bold",12),bg="grey").grid(row=9,column=1)
Pincode=Label(root,text="Pin Code",font=("bold",12),bg="grey").grid(row=10,column=1)
Country=Label(root,text="Country",font=("bold",12),bg="grey").grid(row=11,column=1)
password=Label(root,text="Password",font=("bold",12),bg="grey").grid(row=12,column=1)
#Checkbox
v1=IntVar()
Checkbutton(root,text="Remember me",variable=v1,width=16).grid(row=13,column=2)


#creating input fields
first_name=Entry(root,borderwidth=5).grid(row=1,column=2,ipadx=100)
last_name=Entry(root,borderwidth=5).grid(row=2,column=2,ipadx=100)
emp_id=Entry(root,borderwidth=5).grid(row=3,column=2,ipadx=100)
email=Entry(root,borderwidth=5).grid(row=5,column=2,ipadx=100)
Phone_no=Entry(root,borderwidth=5).grid(row=6,column=2,ipadx=100)
City=Entry(root,borderwidth=5).grid(row=8,column=2,ipadx=100)
State=Entry(root,borderwidth=5).grid(row=9,column=2,ipadx=100)
Pincode=Entry(root,borderwidth=5).grid(row=10,column=2,ipadx=100)
Country=Entry(root,borderwidth=5).grid(row=11,column=2,ipadx=100)
password=Entry(root,borderwidth=5).grid(row=12,column=2,ipadx=100)
#button creation
def myclick():
    #for displaying message box
    tkinter.messagebox.showinfo("Thank you","Your Information submitted successfully!!")
    return
#submit button
submit=Button(root,text="Submit",command=myclick,bg="purple",fg='white').grid(row=14,column=2,padx=50,pady=50)

root.mainloop()
