from tkinter import *
root = Tk()
root.geometry("500x500")
root.resizable(100,100)
root.title("Mini_Lin - Website Blocker")
Label(root, text='WEBSITE BLOCKER', font='times 20 bold').pack()
Label(root, text='Mini_Lin', font='times  20 bold').pack(side=BOTTOM)
host_path = str


def assignwindow():
    global host_path
    host_path = 'C:\Windows\System32\drivers\etc\hosts'
    


def assignapple():
    global host_path
    host_path = '/etc/hosts'



ip_address = '127.0.0.1'
Label(root, text='Enter Website :', font='times 13 bold').place(x=5, y=60)
Websites = Text(root, font='times 10', height='2', width='40', wrap=WORD, padx=5, pady=5)
Websites.place(x=120, y=60)
window = Button(root, text='Windows', font='arial 12 bold', pady=5, command=assignwindow, width=6,
                bg='royal blue1', activebackground='sky blue')
window.place(x=150, y=200)
apple = Button(root, text='MacOS', font='arial 12 bold', command=assignapple, pady=5, width=6, bg='royal blue1',
               activebackground='sky blue')
apple.place(x=250, y=200)


def Blocker():
    website_lists = Websites.get(1.0, END)
    Website = list(website_lists.split(","))
    try:
        with open(host_path, "r+") as host_file:
            file_content = host_file.read()
            for website in Website:
                if website in file_content:
                    Label(root, text='Already Blocked', font='times 12 bold').place(x=200, y=200)
                else:
                    host_file.write("{0} {1}".format(ip_address, website))
                    Label(root, text="Blocked", font='times 12 bold').place(x=230, y=300)
    except:
        Label(root, text="You either don't have permission or you chose the wrong OS").pack(side=BOTTOM)


block = Button(root, text='Block', font='arial 12 bold', pady=5, command=Blocker, width=6, bg='royal blue1',
               activebackground='sky blue')
block.place(x=200, y=100)

root.mainloop()
