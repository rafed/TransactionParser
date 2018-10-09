from tkinter import *
from tkinter import messagebox
import fileParser
import sys, os
import datetime

# root = Tk()

masterWindow = None
outputFolder = ""
msgs = ""

def showMessageText(text, outputLocation):
    global masterWindow, outputFolder, msgs
    outputFolder = outputLocation
    msgs = text

    text = "\n\n"+"*"*75+"\n\n"
    text = text.join(msgs)

    # print("MSG")
    # print (msgs)
    masterWindow = Tk()
    masterWindow.title("File Parser")
    masterWindow.geometry("640x500")
    masterWindow.config(bg ="#828481")
    masterWindow.maxsize(width=640, height=500)
    masterWindow.resizable(width=False, height=False)

    upperFrame = Frame(masterWindow, width=640, height=450)
    upperFrame.pack(side = TOP)

    S = Scrollbar(upperFrame)
    T = Text(upperFrame , height=27)

    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)

    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    T.insert(END, text)
    T.config(state=DISABLED)

    lowerFrame = Frame(masterWindow, width=640, height=50, bg ="#828481")
    lowerFrame.pack(side = BOTTOM)

    okButton = Button(lowerFrame, text="OK", command=okCallback)
    okButton.config( height = 1, width = 15 )
    okButton.place(rely=0.5, relx=0.7, x=0, y=0, anchor="center")
    # okButton.pack( side = LEFT )

    cancelButton = Button(lowerFrame, text="Cancel", command=cancelCallback)
    cancelButton.config( height = 1, width = 15 )
    cancelButton.place(rely=0.5, relx=0.3, x=0, y=0, anchor="center")

    mainloop()

def okCallback():
    global masterWindow, outputFolder, msgs
    dt = datetime.datetime.now()
    dt_str = dt.strftime("%Y-%m-%d_%H.%M.%S")
    outputFolder = outputFolder + "/" + dt_str + "/"
    os.mkdir(outputFolder)
    fileParser.makePdf(msgs, outputFolder)
    fileParser.makeCSV(msgs, outputFolder)
    print ("click!")
    masterWindow.destroy()
    messagebox.showinfo("Information","Files have been created!")

def cancelCallback():
    global masterWindow
    masterWindow.destroy()
    print ("cancel!")



    


