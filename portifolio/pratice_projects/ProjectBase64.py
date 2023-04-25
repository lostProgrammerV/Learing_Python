from tkinter import *
from tkinter import massagebox
import base64
import os

def main_screen():
    
    screen = Tk()
    screen.geometry('375x398')

    #icon
    image_icon=PhotoImage(file='keys.png')
    screen.iconphoto(FALSE, image_icon)

    screen.title('PicApp')

    def reset():
        code.set("")
        text1.delete(1.0,END)

    def encrypt():
        if password.get(text1):
            password=code.get()
            screen1=Toplevel(screen)
            screen1.titlee('encryption')
            screen1.geometry('400x200')
            screen1.configure(bg='#ed38333')

            massage=text1.get(1.0,END)
            encode_massage=massage.encode('ascii')
            base64_bytes=base64.b64decode(encode_massage)
            encrypt=base64_bytes.decode('ascii')

            label(screen1,text='encrypt',font='arial',fg='white',bg='#ed3833').place(x=10,y=0)
            text2=Text(screen1,font='roboto 10',bg='white',relief=GROOVE,wrap=WORD,bd=0)
            text2.place(x=10,y=40,width=380,height=150)

            text2.insert(END, encrypt)
        elif password == '':
           massagebox.showerror("encryption", "Input Password")
        elif password != "1234":
           massagebox.showerror("encryption","Invalid Password")


    def decrypt():
        if password.get(text1):
            password=code.get()
            screen2=Toplevel(screen)
            screen2.titlee('encryption')
            screen2.geometry('400x200')
            screen2.configure(bg='#ed38333')

            massage=text1.get(1.0,END)
            decode_massage=massage.encode('ascii')
            base64_bytes=base64.b64decode(decode_massage)
            decrypt=base64_bytes.decode('ascii')

            label(screen2,text='decrypt',font='arial',fg='white',bg='#00bd56').place(x=10,y=0)
            text2=Text(screen2,font='roboto 10',bg='white',relief=GROOVE,wrap=WORD,bd=0)
            text2.place(x=10,y=40,width=380,height=150)

            text2.insert(END, decrypt)
        elif password == '':
           massagebox.showerror("decryption", "Input Password")
        elif password != "1234":
           massagebox.showerror("decryption","Invalid Password")

    Label(Text='Enter text for encryption and description', fg='black',font=('calibri',13)).place(x=10, y=10)
    text1 = Text(font='roboto 20',bg='white',relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text='Enter secret key for encryption and decryption', fg='black',font=('calibri',13)).place(x=10, y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=('arial',25)).place(x=10,y=200)

    Button(Text='encrypt',height='2',width=23,bg='#ed3833',fg='white',bd=0,command=encrypt).place(x=10,y=250)
    Button(Text='decrypt',height='2',width=23,bg='#00bd56',fg='white',bd=0,command=decrypt).place(x=200,y=250)
    Button(text='reset',height='2',width=50,bg='#1089ff',fg='white',command=reset).place(x=10,y=300)

    screen.mainloop()

main_screen()