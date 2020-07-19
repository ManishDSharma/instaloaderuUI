from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os
from tkinter import simpledialog
import instaloader
from datetime import datetime
import csv
from tkinter.filedialog import askopenfilename

top = Tk()
top.geometry("380x380+500+150")
top.resizable(width=False, height=False)

#instruction menu

def instruct():
    root=tk.Tk()
    root.title("Help")
    root.resizable(width=False, height=False)
    root.geometry("457x400+250+100")
    w = Label(root, text ='Instruction', font = ('helvetica', 30, 'bold'))  
    w.pack()
    instruction="1: Enter your Instagram user name in ‘Login user name’.\n2: Enter target user name/page user name in ‘Target Address’.\n3: Select one option from given options(What you want to download from Target person/page).\n4: Enter the folder name into which the downloads has to be saved in ‘Story Name’.\n5.Enter the project Id in ‘Project Id’(file name will be appended with this project Id).\n6: click on submit.\n7: After submitting  a pop-up box  will open , in this pop-up box you have to select that the target   user/page is public or private.\n7.1: if Target user/Page is Public, Select Public and Click Ok ,it will start downloading.\n7.2: if Target user/page is Private, Select Private and Click Ok, After Clicking Ok it will ask for your Instagram id password, Type your instagram password and Click Ok, it will start downloading."
    msg = Message( root, text = instruction )
    msg.config(font=('helvetica', 10))
    msg.pack()   
    root.mainloop() 
#menu
menu = tk.Menu(top) 
top.config(menu=menu) 
filemenu = tk.Menu(menu) 
menu.add_cascade(label='Help', menu=filemenu) 
filemenu.add_command(label='Instruction', command=instruct) 
filemenu.add_command(label='Exit', command=top.quit)

#ui name
top.title("Instagram Downloader")

canvas1 = Canvas(top, width = 380, height = 380, bg = 'gray90', relief = 'raised')
canvas1.pack()

#name
name = Label(top, text='Dowell Instagram Downloader',bg='#C11B17',fg='white', font=('helvetica', 19, 'bold')) 
canvas1.create_window(190, 20, window=name)

#textbox
label2=tk.Label(top, text = "Login UserName :",bg="#6960EC",fg='white',font=('helvetica', 13, 'bold'))
canvas1.create_window(95, 70, window=label2)

textBox1=tk.Entry(top, width=16,font=('helvetica', 14))
canvas1.create_window(273, 70, window=textBox1)

#combobox
label1= tk.Label(top, text = "Select Options :",width=14,bg='#6960EC',fg='white',font=('helvetica', 13, 'bold'))
canvas1.create_window(95, 120, window=label1)

cmb = ttk.Combobox(top, width=18, values=("PROFILES","STORIES","IGTV","HASHTAG"),font=('helvetica', 13),justify='center')
canvas1.create_window(273, 120, window=cmb)
cmb.set("--Select--")
 
label=tk.Label(top, text = " TargetAddress :",bg="#6960EC",fg='white',font=('helvetica', 13, 'bold'))
canvas1.create_window(95, 170, window=label)


textBox=tk.Entry(top, width=16,font=('helvetica', 14))
canvas1.create_window(273, 170, window=textBox)

label3=tk.Label(top, text = "         Story :        ",bg="#6960EC",fg='white',font=('helvetica', 13, 'bold'))
canvas1.create_window(95, 220, window=label3)

textBox2=tk.Entry(top, width=16,font=('helvetica', 14))
canvas1.create_window(273, 220, window=textBox2)

label4=tk.Label(top, text = "           ID :           ",bg="#6960EC",fg='white',font=('helvetica', 13, 'bold'))
canvas1.create_window(95, 270, window=label4)

textBox3=tk.Entry(top, width=16,font=('helvetica', 14))
canvas1.create_window(273, 270, window=textBox3)

var = IntVar()
global answer
global x
def csvup():
    fp = askopenfilename()
    with open(fp, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        name = []
        for sublist in data:
            for item in sublist:
                name.append(item)
    textBox.insert(0,name)

def radbtn():
    top.deiconify()   
    x=var.get()
    if(cmb.get()=="STORIES"):
        if(x==1):
            answer = simpledialog.askstring("Password", "Please Enter your password", show="*")
            if(answer!=""):
                for i in textBox.get().split():
                    L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                    L.login(textBox1.get(),answer)
                    profile = L.check_profile_id(i)
                    L.download_stories(userids=[profile])
            else:
                messagebox.showerror("Error","Please enter your password")
        elif(x==2):
            for i in textBox.get().split():
                L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                profile = L.check_profile_id(i)
                L.download_stories(userids=[profile])
        else:
            messagebox.showerror("Error","Please Select Private or Public")
            priorpub()
    elif(cmb.get()=="IGTV"):
        if(x==1):
            answer = simpledialog.askstring("Password", "Please Enter your password", show="*")
            if(answer!=""):
                for i in textBox.get().split():
                    L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                    L.login(textBox1.get(),answer)
                    profile = instaloader.Profile.from_username(L.context,i)
                    L.download_igtv(profile, fast_update=False, post_filter=None)
            else:
                messagebox.showerror("Error","Please enter your password")
        elif(x==2):
            for i in textBox.get().split():
                L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                profile = instaloader.Profile.from_username(L.context,i)
                L.download_igtv(profile, fast_update=False, post_filter=None)
        else:
            messagebox.showerror("Error","Please Select Private or Public")
            priorpub()
    elif(cmb.get()=="PROFILES"):
        if(x==1):
            answer = simpledialog.askstring("Password", "Please Enter your password", show="*")
            if(answer!=""):               
                for i in textBox.get().split():
                    L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                    L.login(textBox1.get(),answer)
                    profile = instaloader.Profile.from_username(L.context,i)
                    L.download_profiles(set([profile]), profile_pic=True, posts=True, tagged=False, igtv=False, highlights=False, stories=False,fast_update=False, post_filter=None, storyitem_filter=None, raise_errors=False)
            else:
                messagebox.showerror("Error","Please enter your password") 
        elif(x==2):
            for i in textBox.get().split():
                L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                profile = instaloader.Profile.from_username(L.context,i)
                L.download_profiles(set([i]), profile_pic=True, posts=True, tagged=False, igtv=False, highlights=False, stories=False,fast_update=False, post_filter=None, storyitem_filter=None, raise_errors=False)
        else:
            messagebox.showerror("Error","Please Select Private or Public")
            priorpub()
    elif(cmb.get()=="HASHTAG"):
        if(x==1):
            answer = simpledialog.askstring("Password", "Please Enter your password", show='*')
            if(answer!=""):
                for i in textBox.get().split():
                    L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                    L.login(textBox1.get(),answer)
                    hashtag = instaloader.Hashtag.from_name(L.context,i)
                    for post in hashtag.get_posts():
                        L.download_post(post, target="#"+hashtag.name)
            else:
                messagebox.showerror("Error","Please enter your password")
        elif(x==2):
            for i in textBox.get().split():
                L=instaloader.Instaloader(download_comments=False,compress_json=False,save_metadata=False,
                              dirname_pattern="C:/"+textBox1.get()+" "+str(datetime.now().date())+" "+textBox2.get()+" "+textBox3.get()+"/"+i)
                hashtag = instaloader.Hashtag.from_name(L.context,i)
                for post in hashtag.get_posts():
                    L.download_post(post, target="#"+hashtag.name)
        else:
            messagebox.showerror("Error","Please Select Private or Public")
            priorpub()
    else:
        pass

def priorpub():
    top.iconify()
    root=Toplevel(top)
    root.geometry("100x100+600+200")
    root.resizable(width=False,height=False)
    root.title("Private or Public?")
    R1 = Radiobutton(root, text="Private",  value=1,variable=var)
    R1.grid(row=1,column=1)
    R2 = Radiobutton(root, text="Public",  value=2,variable=var)
    R2.grid(row=2,column=1)
    btn2 = tk.Button(root,text='OK',width=7, command=radbtn, bg='#4AA02C', fg='white', font=('helvetica', 14, 'bold'))
    btn2.grid(row=3,column=1)
    root.grab_set()
    root.grab_release()
    root.mainloop()
def submit():
    L = instaloader.Instaloader()
    if (textBox1.get().lower() !=""):
        if (cmb.get() !="--Select--"):
            if (textBox.get().lower() !=""):           
                if (textBox2.get().lower() !=""):
                    if (textBox3.get().lower() !=""):
                        priorpub()
                    else:
                        messagebox.showerror("Error","Please enter your unique id") 
                else:
                    messagebox.showerror("Error","Please enter your story name")
            else:
                messagebox.showerror("Error","Please enter appropriate profile username")
        else:
            messagebox.showerror("Error","Please select an option")
    else:
        messagebox.showerror("Error","Please enter your appropriate name") 

def quit_msg():
    qw=Tk()
    frame1 = Frame(qw, highlightbackground="green", highlightcolor="green",highlightthickness=1, bd=0)
    frame1.pack()
    qw.overrideredirect(1)
    qw.geometry("200x70+600+250")
    lbl = Label(frame1, text="Are you sure you want to quit?")
    lbl.pack()
    yes_btn = Button(frame1, text="Yes", bg="light blue", fg="red",command=quit, width=10)
    yes_btn.pack(padx=10, pady=10 , side=LEFT)
    no_btn = Button(frame1, text="No", bg="light blue", fg="red",command=qw.destroy, width=10)
    no_btn.pack(padx=10, pady=10, side=LEFT)
    qw.mainloop()
    
#button submit
btn = tk.Button(top,text='SUBMIT',width=8, command=submit, bg='#4AA02C', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(85, 330, window=btn)

#button upload
btn2 = tk.Button(top,text='IMPORT',width=8, command=csvup, bg='#4AA02C', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(205, 330, window=btn2)

#button quit
btn1 = tk.Button(top,text='QUIT',width=6, command=quit_msg, bg='#4AA02C', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(315, 330, window=btn1)

top.mainloop()
