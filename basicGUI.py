#Import tkinter library
from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox     # for showing message

# Function to handle correct of incorrect password
def handle_login():
    email=email_input.get()
    password=password_input.get()

    if email=='mrinal@gmail.com' and password=='1234':
        messagebox.showinfo('Yay!!','Login successful')
    else:
        messagebox.showerror('Error','Login Failed')

root = Tk()
root.title('Login Form')
root.iconbitmap('loginicon.ico')
root.geometry('350x500')
root.configure(background='#0096DC')   #for applying background color to UI

#Adding image
img=Image.open('travel-logo.png')
resized_img=img.resize((70,70))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))

#Adding text into UI
text_label=Label(root,text='Travel',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

#Adding Email as text
email_label=Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

#Taking user input as email
email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))


#Adding text as Password into  UI
password_label=Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

#Taking password as user input
password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))



#Adding button into UI
login_btn=Button(root,text='Login Here',bg='white',fg='black',width=30,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))

#This function is used to remain continuous UI
root.mainloop()