from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
def enc(filename,password):
    try:
        import pyAesCrypt
        pyAesCrypt.encryptFile(filename, (filename + ".enc"), password)
        print("Encryption done with password: ",password)
        pwdbox.delete(0,END)
        return 1
    except:
        messagebox.showerror(title="error",message="some error occured")

def dec(filename,password):
    try:
        import pyAesCrypt
        f = filename[:-4]
        pyAesCrypt.decryptFile(filename, f, password)
        print("Decryption done with password: ",password)
        pwdbox.delete(0, END)
        return 1
    except:
        messagebox.showerror(title="error",message="Wrong password")
def fi(a):
    file = askopenfilename()
    if(file==''):
        return 0
    password=pwdbox.get()
    if(password==''):
        messagebox.Message(title="!!!!", message="Password is empty")
    if(a==1):
        enc(file,password)
    else:
        dec(file,password)
def p1():
    fi(1)
def p2():
    fi(2)


root = Tk()
logo = PhotoImage(file='logo1.png')
root.configure(bg="black")
root.geometry("300x220")
root.title("File enc/dec")
root.iconphoto(False,logo)
Label(text="By s0ulix", bg="red", width="50", height="2", font=("Helvetica", 13), fg="white").pack()
Label(root, text = 'Please enter paswsword before proceeding!!!').pack()
Button(text="Encrypt", height="2", width="30", font=("Helvetica", 13), command=p1).pack()
Button(text="Decrypt", height="2", width="30", font=("Helvetica", 13), command=p2).pack()
Label(root, text = 'Password').pack()
pwdbox = Entry(root)
pwdbox.pack()
root.mainloop()
