from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askdirectory
import messageTextScreen
import fileParser


inputFile = ""
outputFolder = ""

def inputCallBack():
	global inputFile, outputFolder
	inputFile = askopenfilename()
	if(len(inputFile)==0):
		inputFileLabel.config(text="No File Chosen")
	elif(len(inputFile)>30):
		inputFileLabel.config(text=inputFile[0:31]+"...")
	else:
		inputFileLabel.config(text=inputFile)
	print (inputFile)

def outputCallBack():
	global inputFile, outputFolder
	outputFolder = askdirectory()
	if(len(outputFolder)==0):
		outputFolderLabel.config(text="No Directory Chosen")
	elif(len(outputFolder)>30):
		outputFolderLabel.config(text=outputFolder[0:31]+"...")
	else:
		outputFolderLabel.config(text=outputFolder)
	print (outputFolder)

def runCallBack():
	print("run")
	if(len(inputFile)>0 and len(outputFolder)>0):
		text = fileParser.parseFile(inputFile,outputFolder)
		if text==[]:
			messagebox.showerror("Error", "Problem in File Format")
		else:
			messageTextScreen.showMessageText(text, outputFolder)
	else:
		print(len(inputFile))
		print(len(outputFolder))
		messagebox.showerror("Error", "Choose Input File and Output Folder")
def onEnter(e):
    buttonRun['background'] = '#E85A32'

def onLeave(e):
    buttonRun['background'] = 'SystemButtonFace'

masterWindow = Tk()
masterWindow.title("File Parser")
masterWindow.geometry("480x320")
masterWindow.config(bg ="#828481")
masterWindow.maxsize(width=480, height=320)
masterWindow.resizable(width=False, height=False)

#Left Frame and its contents
upperFrame = Frame(masterWindow, width=480, height = 260 , bg="#828481") #, highlightthickness=2, highlightbackground="#111")
upperFrame.grid(row=0, column=0, padx=0, pady=0, sticky=N+S)

imageEx = PhotoImage(file = 'parser.png')
# imageEx = imageEx.subsample(2, 2)
Label(upperFrame, image=imageEx).grid(row=0, column=0, padx=0, pady=0)

btnFrame = Frame(upperFrame, width=480, height = 200, bg ="#828481") #bg="#E8E8E8"
btnFrame.grid(row=1, column=0, padx=0, pady=15)

#LABEL
inputLabel = Label(btnFrame, text="Input file: ", anchor='w')
inputLabel.config( height = 1, width = 20, bg ="#828481")
inputLabel.grid(row=0, column=0, padx=0, pady=0)

outputLabel = Label(btnFrame, text="Output location: ", anchor='w')
outputLabel.config( height = 1, width = 20, bg ="#828481")
outputLabel.grid(row=1, column=0, padx=0, pady=0)

# Path

inputFileLabel = Label(btnFrame, text="No File Chosen", anchor='w')
inputFileLabel.config( height = 1, width = 30, bg ="#828481")
inputFileLabel.grid_columnconfigure(1, minsize=700)
inputFileLabel.grid(row=0, column=1, padx=0, pady=0) #, columnspan=4)

outputFolderLabel = Label(btnFrame, text="No Directory Chosen", anchor='w')
outputFolderLabel.config( height = 1, width = 30, bg ="#828481")
outputFolderLabel.grid(row=1, column=1, padx=0, pady=0)#, columnspan=4)

# BUTTONS
buttonInput = Button(btnFrame, text ="Select File", command=inputCallBack)
buttonInput.config( height = 1, width = 10 ) #bg='#E85A32'
buttonInput.grid(row=0, column=2, padx=0, pady=1)

buttonOutput = Button(btnFrame, text ="Select Folder", command=outputCallBack)
buttonOutput.config( height = 1, width = 10 )
buttonOutput.grid(row=1, column=2, padx=0, pady=1)

lowerFrame = Frame(masterWindow, width=480, height = 160, bg="#828481" )#, highlightthickness=2, highlightbackground="#111")
lowerFrame.grid(row=1, column=0, padx=0, pady=0, sticky=N+S)

buttonRun = Button(lowerFrame, text ="Run", command=runCallBack)
buttonRun.config( height = 1, width = 10 )
buttonRun.grid(row=0, column=0, padx=100, pady=30)
buttonRun.bind("<Enter>", onEnter)
buttonRun.bind("<Leave>", onLeave)

mainloop()
