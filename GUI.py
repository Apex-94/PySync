from functools import partial
from tkinter import *
user_ip=[]
user_path=[]
def cleartb():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
def printIP():
    user_ip.append(E1.get())
    user_ip.append(E2.get())
    user_ip.append(E3.get())
    print(*user_ip) #just to check input
def cleartb2():
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)
def printpath():
    user_path.append(E4.get())
    user_path.append(E5.get())
    user_path.append(E6.get())
    print(*user_path) #just to check input

root = Tk() #For 1st window
root.configure(background="#a1dbcd")
root.title("Set IP")
root.wm_iconbitmap(r'C:\Users\User\Desktop\icon2.ico')#path to icon file

    
def create_window():
        global user_path
        window = Tk()#For 2nd window
        window.configure(background="#a1dbcd")
        window.title("Set Path")
        window.wm_iconbitmap(r'C:\Users\User\Desktop\icon2.ico')#path to icon file
        label4 = Label( window, text="Enter path User 1:",fg="#383a39",bg="#a1dbcd")
        E4 = Entry(window, bd =5)
        label5 = Label( window, text="Enter path User 2:",fg="#383a39",bg="#a1dbcd")
        E5 = Entry(window, bd =5)
        label6 = Label( window, text="Enter path User 3:",fg="#383a39",bg="#a1dbcd")
        E6 = Entry(window, bd =5)
        submit2 = Button(window, text ="Submit",command=printpath)
        Delete_button = Button(window, text = 'Clear all', command = cleartb2)#To clear text field
        user_path = [x.strip(' ') for x in user_path]#strip sapace
        label4.pack()
        E4.pack()
        label5.pack()
        E5.pack()
        label6.pack()
        E6.pack()
        submit2.pack(side =BOTTOM)
        Delete_button.pack()
        window.geometry("300x250")
        window.mainloop()

label1 = Label( root, text="Enter IP user 1:",fg="#383a39",bg="#a1dbcd")
E1 = Entry(root, bd =5)
label2 = Label( root, text="Enter IP user 2:",fg="#383a39",bg="#a1dbcd")
E2 = Entry(root, bd =5)
label3 = Label( root, text="Enter IP user 3:",fg="#383a39",bg="#a1dbcd")
E3 = Entry(root, bd =5)

Delete_button = Button(root, text = 'Clear all', command = cleartb)#To clear text field
Delete_button.pack()

user_ip = [x.strip(' ') for x in user_ip]# Strip space
next_window=Button(root,text='Next',width=5,command=create_window).place(x=250,y=200)#Call secound window when clicked
submit = Button(root, text ="Submit", command = printIP)
        
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
submit.pack(side =BOTTOM)
root.geometry("300x250")
root.mainloop()
