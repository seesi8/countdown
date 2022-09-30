# this is at top

import tkinter as tk
import time
from tkinter import *
from PIL import Image,ImageTk
import os
import time
import threading
from tkinter.filedialog import askopenfilename
import pygame
from tkinter import Tk
from datetime import datetime
from datetime import date
import random
import turtle
from functools import partial
import itertools
import sys
import os, shutil
import cv2
import shutil
import os, os.path
root_1   = "data\frame"
number = "0"
path = root_1+number+".jpg"


window = tk.Tk()
label = tk.Label(master=window,text="time goes there -->",borderwidth = 0)
label2 = tk.Label(master=window,text="date goes there -->",borderwidth = 0)
currentframe = 0
entry = tk.Entry(borderwidth = 0)
entry2 = tk.Entry(borderwidth = 0)

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('data\Crab.mp3')
sound.set_volume(1.0)   # Now plays at 90% of full volume.
wow = pygame.mixer.Sound('data\wow.mp3')
wow.set_volume(1.0)   # Now plays at 90% of full volume.
bob = 1
infinity = 0
u = 0

def infinity_1():
    global infinity
    infinity = 0
    while True:
        infinity += 1
def songs():
    loops = 0
    global infinity
    global sound
    #  'none','crab rave','Auld Lang Syne','it is the final countdown','paca song'
    sound.stop()
    if state5 == 'none':
        pygame.mixer.music.stop()
    if state5 == 'crab rave':
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Music\Crab.mp3")
    if state5 == 'Auld Lang Syne':
        pygame.mixer.music.stop()
        pygame.mixer.music.load("newyears.mp3")
    if state5 == 'it is the final countdown':
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Music\countdown.mp3")
    if state5 == 'paca song':
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Music\paca.mp3")
    if state5 == 'custom':
        pygame.mixer.music.stop()
        button8 = tk.Button(joey,command=threading.Thread(target=soundpicker).start,text = 'click here to upload file')
        button8.grid(row=2,column=1)
    if state5 != 'none':
        pygame.mixer.music.play(infinity)
def soundpicker():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    musicfile = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    pygame.mixer.music.load(musicfile)
    threading.Thread(target=songs).start()
def file():
    global currentframe
    global infinity
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    split_string = filename
    split_string = filename.split("/", 1000000)
    substring = split_string[len(split_string)-1]
    dir_path = 'custom'
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print()
 
    # Read the video from specified path 
    cam = cv2.VideoCapture(filename)
  
    try: 
        # creating a folder named data 
        if not os.path.exists('custom'): 
            os.makedirs('custom')
  
    # if not created then raise error 
    except OSError:
        print()
  
    # frame 
    currentframe = 0
    ret,frame = cam.read() 
    while ret: 
      
        # reading from frame 
        ret,frame = cam.read() 
  
        if ret: 
            # if video is still left continue creating images 
            name = './custom/frame' + str(currentframe) + '.jpg'
  
            # writing the extracted images 
            cv2.imwrite(name, frame) 
  
            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += 1
        else:
            global button7
            button7.grid_forget()
            threading.Thread(target=chng5 ,args=("custom","19588","5672","data3/crab_rave")).start()
  
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 
def chng1(folder,maxframes,soundpoint,soundspot):
    global u
    global state4
    u += 1
    img.grid(columnspan=5,row=1, column=0)
    while state4 == 'panda':
        global path
        global number
        global root_1
        root_1   = "/frame"
        time.sleep(.01)
        number = str(number)
        path = folder+root_1+str(number)+".jpg"
        photo2 = ImageTk.PhotoImage(Image.open(path))
        img.config(image = photo2) 
        img.photo_ref = photo2 # keep a reference
        number = int(number)
        u += 1
        if u == 5320:
            if state6 == 'true':
                sound.stop()
                wow = pygame.mixer.Sound(soundspot)
                wow.play()
                time.sleep(2)
                wow.stop()
                u += 1
                sound.play()
        number = int(number)
        typenumber = type(number)
        if number == 6141:
            number = 0
            u = 0
        img.update_idletasks()
        number = int(number)
        number += 1
        number = str(number)
        path = folder+root_1+number+'.jpg'
def chng5(folder,maxframes,soundpoint,soundspot):
    global u
    global state4
    global currentframe
    u += 1
    while state4 == 'custom':
        global path
        global number
        global root_1
        root_1   = "/frame"
        time.sleep(.01)
        number = str(number)
        path = folder+root_1+str(number)+".jpg"
        photo2 = ImageTk.PhotoImage(Image.open(path))
        img.config(image = photo2) 
        img.photo_ref = photo2 # keep a reference
        number = int(number)
        joeyisawesome = int(currentframe)-1
        if int(number) == int(joeyisawesome):
            number = 0
            u = 0
        img.update_idletasks()
        number = int(number)
        number += 1
        number = str(number)
        path = folder+root_1+number+'.jpg'
def chng2(folder,maxframes,soundpoint,soundspot):
    global u
    global state4
    u += 1
    while state4 == 'crab rave video':
        global path
        global number
        global root_1
        root_1   = "/frame"
        time.sleep(.01)
        number = str(number)
        path = folder+root_1+str(number)+".jpg"
        photo2 = ImageTk.PhotoImage(Image.open(path))
        img.config(image = photo2) 
        img.photo_ref = photo2 # keep a reference
        number = int(number)
        u += 1
        if u == 5672:
            if state6 == 'true':
                sound.stop()
                wow = pygame.mixer.Sound(soundspot)
                wow.play()
                time.sleep(2)
                wow.stop()
                u += 1
                sound.play()
        if number == currentframe:
            number = 0
            u = 0
        img.update_idletasks()
        number = int(number)
        number += 1
        number = str(number)
        path = folder+root_1+number+'.jpg'
def chng3(folder,maxframes,soundpoint,soundspot):
    global u
    global state4
    u += 1
    while state4 == 'puppies':
        global path
        global number
        global root_1
        root_1   = "/frame"
        time.sleep(.01)
        number = str(number)
        path = folder+root_1+str(number)+".jpg"
        photo2 = ImageTk.PhotoImage(Image.open(path))
        img.config(image = photo2) 
        img.photo_ref = photo2 # keep a reference
        number = int(number)
        u += 1
        if u == 5672:
            if state6 == 'true':
                sound.stop()
                wow = pygame.mixer.Sound(soundspot)
                wow.play()
                time.sleep(2)
                wow.stop()
                u += 1
                sound.play()
        if number == 19588:
            number = 0
            u = 0
        img.update_idletasks()
        number = int(number)
        number += 1
        number = str(number)
        path = folder+root_1+number+'.jpg'

        


#_________________________________

def start():
    global total4
    p = entry.get()
    p2 = entry2.get()



    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    hours1 = now.strftime("%H")

    minnuts1 = now.strftime("%M")

    seconds1 = now.strftime("%S")

    #defining hour, 1
    hours1 = int(hours1)
    minnuts1 = int(minnuts1)
    seconds1 = int(seconds1)
    hours1 = hours1-1
    minnuts1 = minnuts1-1
    seconds1 = seconds1-1



    today = date.today()
    x = type(today)


    #year month days
    year = now.strftime("%Y")

    months = now.strftime("%m")

    days = now.strftime("%d")

    #seconds for the year
    year = int(year)
    year = (year-1) * 365.25 * 24 * 60 * 60
    #_________________________________
    #finding the month
    months = int(months)
    months = months - 1
    #___________________
    #how many days per month
    if months == 0:
        months = 12
    if months == 1:
        months = 31
    if months == 2:
        months = 28
    if months == 3:
        months = 31
    if months == 4:
        months = 30
    if months == 5:
        months = 31
    if months == 6:
        months = 30
    if months == 7:
        months = 31
    if months == 8:
        months = 31
    if months == 9:
        months = 31
    if months == 10:
        months = 31
    if months == 11:
        months = 30
    if months == 12:
        months = 30
    # _______________
    #how many seconds are in the month
    months = months * 24 * 60 * 60

    days = int(days)
    days = days - 1
    days = days * 24 * 60 *60
    total3 = (hours1*60*60)+(minnuts1*60)+(seconds1)

    total2 = year + months + days + total3 # this works this shows current seccont time




    until = p

    until2 = p2


    months2,days2,years2 = until2.split('/')

    years2 = int(years2)
    years2 = years2 - 1
    years2 = years2 * 365.25 * 24 * 60 * 60
    months2 = int(months2)
    months2 = months2 -1

    if months2 == 0:
        months2 = 12
    if months2 == 1:
        months2 = 31
    if months2 == 2:
        months2 = 28
    if months2 == 3:
        months2 = 31
    if months2 == 4:
        months2 = 30
    if months2 == 5:
        months2 = 31
    if months2 == 6:
        months2 = 30
    if months2 == 7:
        months2 = 31
    if months2 == 8:
        months2 = 31
    if months2 == 9:
        months2 = 31
    if months2 == 10:
        months2 = 31
    if months2 == 11:
        months2 = 30
    if months2 == 12:
        months2 = 30

    months2 = months2 * 24 * 60 * 60

    days2 = int(days2)
    days2 = days2 - 1
    days2 = days2 * 24 * 60 *60

    total5 = days2+months2+years2



    my_string = until
    hour,minnuts = my_string.split(':')
    hour = int(hour)
    hour = (hour-1) * 60 *60
    minnuts = int(minnuts)
    minnuts = (minnuts-1) * 60
    total = hour + minnuts

    total=total+total5
        #this works       
    total4 = total-total2


    
    entry.delete(0, tk.END)
    entry.insert(0, total4)
    label = tk.Label(text="time left in seconds")
    label.update_idletasks()
    
    threading.Thread(target=countdown).start()

def countdown():
    global total4
    while total4 > 0:
        total4 += -1
        entry.delete(0, tk.END)
        entry.insert(0, total4)
        entry.update_idletasks()
        time.sleep(1)
        if total4 <= 0:
            t = turtle.Turtle()
            t.speed(0)

            def pen(color):
                t.color(color)

            pen('red')

            def move():
                t.pu()
                x = random.randint(-165,165)
                y = random.randint(-165,165)
                t.goto(x,y)
                t.pd()

            def sky(colour):
                 wn = turtle.Screen()
                 wn.bgcolor(colour)

            sky('#10102a')

            def firework(size):
                for num in range(20):
                     t.fd(size)
                     t.rt(180-(360/20))

            # Begin Config #
            C_BRIGHT_MIN = 0x30
            C_BRIGHT_MAX = 0xef
            F_SIZE_MIN = 20
            F_SIZE_MAX = 200
            FIREWORK_PER_CLEAR = 5
            # End Config #

            while True:
                # this generates a random color sequence using RGB
                color_r = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
                color_g = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
                color_b = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
                pen('#'+color_r+color_g+color_b)
                for i in range(FIREWORK_PER_CLEAR):
                    firework(random.randint(F_SIZE_MIN, F_SIZE_MAX))
                    move()
                t.clear()
            
def sam():
    global state3
    global state4
    global state5
    global state6

    def togglebutton3(icycle3=itertools.cycle(['red','orange','yellow','green','blue','purple','strobe','white','black'])):
        global state3
        state3 = next(icycle3)
        threading.Thread(target=background_color).start()
        button3['text'] = str(state3)
    def togglebutton4(icycle4=itertools.cycle(['none','panda','crab rave video','puppies','custom'])):
        global state4
        state4 = next(icycle4)
        threading.Thread(target=video).start()
        button4['text'] = str(state4)
    def togglebutton5(icycle5=itertools.cycle(['none','crab rave','Auld Lang Syne','it is the final countdown','paca song','custom'])):
        global state5
        state5 = next(icycle5)
        threading.Thread(target=songs).start()
        button5['text'] = str(state5)
    def togglebutton6(icycle6=itertools.cycle(['true','false'])):
        global state6
        state6 = next(icycle6)
        button6['text'] = str(state6)
    global bob
    global joey
    threading.Thread(target=togglebutton3)
    threading.Thread(target=togglebutton4)
    threading.Thread(target=togglebutton5)
    threading.Thread(target=togglebutton6)
    if bob == 1:
        bob += 1
        joey = tk.Tk()
        joey.geometry("+100+100")
        button3 = tk.Button(joey, text="background color", command=togglebutton3)
        button3.grid(row=0, column=0, sticky="nsew")
        button4 = tk.Button(joey, text="video", command=togglebutton4)
        button4.grid(row=1, column=0, sticky="nsew")
        button5 = tk.Button(joey, text="song", command=togglebutton5)
        button5.grid(row=2, column=0, sticky="nsew")
        button6 = tk.Button(joey, text="sound effects", command=togglebutton6)
        button6.grid(row=3, column=0, sticky="nsew")

        joey.mainloop()
    if bob == 2:
        bob = 1
        joey.destroy()
        bob = 1
def sam2():
    threading.Thread(target=sam).start()
def background_color():
    global state3
    while True:
        if state3 == 'red':
            window.configure(background='red')
            entry.configure(background='red')
            entry.configure(foreground="white")
            entry2.configure(background='red')
            entry2.configure(foreground="white")
            btn.configure(background='red')
            btn.configure(foreground="white")
            label2.configure(background='red')
            label2.configure(foreground="white")
            label.configure(background='red')
            label.configure(foreground="white")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'orange':
            window.configure(background='orange')
            entry.configure(background='orange')
            entry.configure(foreground="white")
            entry2.configure(background='orange')
            entry2.configure(foreground="white")
            btn.configure(background='orange')
            btn.configure(foreground="white")
            label2.configure(background='orange')
            label2.configure(foreground="white")
            label.configure(background='orange')
            label.configure(foreground="white")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'yellow':
            window.configure(background='yellow')
            entry.configure(background='yellow')
            entry.configure(foreground="black")
            entry2.configure(background='yellow')
            entry2.configure(foreground="black")
            btn.configure(background='yellow')
            btn.configure(foreground="black")
            label2.configure(background='yellow')
            label2.configure(foreground="black")
            label.configure(background='yellow')
            label.configure(foreground="black")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'green':
            window.configure(background='green')
            entry.configure(background='green')
            entry.configure(foreground="white")
            entry2.configure(background='green')
            entry2.configure(foreground="white")
            btn.configure(background='green')
            btn.configure(foreground="white")
            label2.configure(background='green')
            label2.configure(foreground="white")
            label.configure(background='green')
            label.configure(foreground="white")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'blue':
            window.configure(background='blue')
            entry.configure(background='blue')
            entry.configure(foreground="white")
            entry2.configure(background='blue')
            entry2.configure(foreground="white")
            btn.configure(background='blue')
            btn.configure(foreground="white")
            label2.configure(background='blue')
            label2.configure(foreground="white")
            label.configure(background='blue')
            label.configure(foreground="white")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'purple':
            window.configure(background='purple')
            entry.configure(background='purple')
            entry.configure(foreground="white")
            entry2.configure(background='purple')
            entry2.configure(foreground="white")
            btn.configure(background='purple')
            btn.configure(foreground="white")
            label2.configure(background='purple')
            label2.configure(foreground="white")
            label.configure(background='purple')
            label.configure(foreground="white")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'black':
            window.configure(background='black')
            entry.configure(background='black')
            entry.configure(foreground="white")
            entry2.configure(background='black')
            entry2.configure(foreground="white")
            btn.configure(background='black')
            btn.configure(foreground="white")
            label2.configure(background='black')
            label2.configure(foreground="white")
            label.configure(background='black')
            label.configure(foreground="white")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update
        if state3 == 'white':
            window.configure(background='white')
            window.configure(background='white')
            entry.configure(background='white')
            entry.configure(foreground="black")
            entry2.configure(background='white')
            entry2.configure(foreground="black")
            btn.configure(background='white')
            btn.configure(foreground="black")
            label2.configure(background='white')
            label2.configure(foreground="black")
            label.configure(background='white')
            label.configure(foreground="black")
            entry.update()
            entry2.update()
            btn.update()
            label2.update()
            label.update()
            window.update()
        if state3 == 'strobe':
            threading.Thread(target=strobe).start()
            print('hello-ish')
def strobe():
    global state3
    print('hello')
    while state3 == 'strobe':
        window.configure(background='black')
        entry.configure(background='black')
        entry.configure(foreground="white")
        entry2.configure(background='black')
        entry2.configure(foreground="white")
        btn.configure(background='black')
        btn.configure(foreground="white")
        label2.configure(background='black')
        label2.configure(foreground="white")
        label.configure(background='black')
        label.configure(foreground="white")
        entry.update()
        entry2.update()
        btn.update()
        label2.update()
        label.update()
        window.update
        time.sleep(.1)
        window.configure(background='white')
        window.configure(background='white')
        entry.configure(background='white')
        entry.configure(foreground="black")
        entry2.configure(background='white')
        entry2.configure(foreground="black")
        btn.configure(background='white')
        btn.configure(foreground="black")
        label2.configure(background='white')
        label2.configure(foreground="black")
        label.configure(background='white')
        label.configure(foreground="black")
        entry.update()
        entry2.update()
        btn.update()
        label2.update()
        label.update()
        window.update()
        time.sleep(.1)
def video():
        global state4
        global joey
        global button7
        button7 = tk.Button(joey,command=threading.Thread(target=file).start,text = 'click here to upload file')
        if state4 == 'panda':
            threading.Thread(target=chng1 ,args=("data","6141","5320","data\wow.mp3")).start()
        if state4 == 'puppies':
            button7.grid_forget()
            threading.Thread(target=chng3 ,args=("data2","19588","5672","data2\puppy.mp3")).start()
        if state4 == 'none':
            button7.grid_forget()
            img.grid_forget()
        if state4 == 'crab rave video':
            button7.grid_forget()
            threading.Thread(target=chng2 ,args=("data3","19588","5672","data3/crab_rave")).start()
        if state4 == 'custom':
            button7.grid(row=1,column=1)
        if state4 != 'custom':
            deleat
def deleat():
    global button7
    button7.grid_forget
    

    
window.geometry("+100+100")# -1800 for dual moniters
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=300, weight=1)
btn = tk.Button(master=window,  text="hello", command=start)
btn.grid(row=0, column=0, sticky="nsew")
label.grid(row=0, column=1,)
entry.grid(row=0, column=2, sticky="nsew")
label2.grid(row=0, column=3,sticky="nsew")
entry2.grid(row=0, column=4, sticky="nsew")
photo = ImageTk.PhotoImage(Image.open("data/frame1.jpg"))
img = Label(window,image = photo)
upload = Button(window, text= "⚙️" ,height = 3, width = 12, command=sam2)
upload.grid(row=1,column=4,sticky="se")
upload.config(font=("Courier", 10))
threading.Thread(target=start)
threading.Thread(target=infinity).start
threading.Thread(target=strobe)
threading.Thread(target=sam)
threading.Thread(target=file)
threading.Thread(target=countdown)
threading.Thread(target=background_color)
window.configure(background='black')
window.configure(background='black')
entry.configure(background='black')
entry.configure(foreground="white")
entry2.configure(background='black')
entry2.configure(foreground="white")
btn.configure(background='black')
btn.configure(foreground="white")
label2.configure(background='black')
label2.configure(foreground="white")
label.configure(background='black')
label.configure(foreground="white")
window.mainloop()

#threading.Thread(target=chng).start()
