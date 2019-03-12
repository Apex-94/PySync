import sys
from tkinter import *
from tkinter import filedialog
from tkinter import Menu
window = Tk()
pathlabel=Label()
pathlist=[]
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
    
def DisplayDir(Var):
    feedback = filedialog.askdirectory()
    Var.set(feedback)
    
def browse_button():
    filename = filedialog.askdirectory()
    Server_window.pathlabel.config(text=filename)
    pathlist.append=filename
    print(*pathlist)
    

def Server_window():
    window_server=Toplevel()
    window_server.configure(background="#a1dbcd")
    window_server.title("Server")
    window.wm_iconbitmap(r'C:\Users\User\Desktop\icon2.ico')
    Browse_button = Button(window_server, text = 'Select folder',width=10,height=1,command=browse_button).place(x=250,y=100)
    pathlabel= Label(window_server)
    pathlabel.place(x=100,y=100)
    window_server.geometry("600x300")
    window_server.mainloop()
    
def Client_window():
    window_Client=Toplevel()
    window_Client.configure(background="#a1dbcd")
    window_Client.title("Server")
    window_Client.wm_iconbitmap(r'C:\Users\User\Desktop\icon2.ico')
    window_Client.geometry("300x300")
    window_Client.mainloop()
    
def exit_1():
    sys.exit()
    
getpath=StringVar()
window.configure(background="#a1dbcd")
window.title("PysYnc")
window.wm_iconbitmap(r'C:\Users\User\Desktop\icon2.ico')
menu = Menu(window)
new_item = Menu(menu,tearoff=False)
new_item.add_command(label='Exit',command=exit_1)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
Server_button = Button(window, text = 'Server',width=20,height=3,command=Server_window)
Server_button.place(x=80,y=100)
createToolTip(Server_button, "YOUR MESSAGE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
Client_button = Button(window, text = 'Client',width=20,height=3,command=Client_window)
Client_button.place(x=80,y=20)
createToolTip(Client_button, "YOUR MESSAGE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
window.geometry("300x300")
window.mainloop()
