from tkinter import scrolledtext

import pytesseract
import tkinter
import PhotoReaderLauncherAndCommands

mainWindow = tkinter.Tk()
mainWindow.title("Photo Reader")
mainWindow.geometry("500x500")

leftArrowIconImage = tkinter.PhotoImage(file=r"Assets/leftArrowIconImage.png")
rightArrowIconImage = tkinter.PhotoImage(file=r"Assets/rightArrowIconImage.png")

filepathEntryWidget = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
filepathEntryWidget.pack(side=tkinter.TOP, padx=15, pady=15)
filepathEntryWidget.place(x=117, y=38, width=170, height=22)

browseFilesButton = tkinter.Button(mainWindow, text="Browse Files", command=PhotoReaderLauncherAndCommands.browseFilesCommand)
browseFilesButton.pack(side=tkinter.TOP, padx=10, pady=50)
browseFilesButton.place(x=300, y=35)

analyzeImageText = tkinter.Button(mainWindow, text="Analyze Image Text", command=PhotoReaderLauncherAndCommands.analyzeImageTextCommand)
analyzeImageText.pack(side=tkinter.TOP, padx=10, pady=50)
analyzeImageText.place(x=120, y=78)

clearButton = tkinter.Button(mainWindow, text="Clear Image and Text", command=PhotoReaderLauncherAndCommands.clearImageAndTextCommand)
clearButton.pack(side=tkinter.TOP, padx=10, pady=50)
clearButton.place(x=250, y=78)

leftArrowButton = tkinter.Button(mainWindow, image=leftArrowIconImage, command=PhotoReaderLauncherAndCommands.leftArrowCommand)
leftArrowButton.pack(side=tkinter.TOP, padx=10, pady=50)
leftArrowButton.place(x=185, y=120, width=40)

rightArrowButton = tkinter.Button(mainWindow, image=rightArrowIconImage, command=PhotoReaderLauncherAndCommands.rightArrowCommand)
rightArrowButton.pack(side=tkinter.TOP, padx=10, pady=50)
rightArrowButton.place(x=250, y=120, width=40)

outputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=19, state=tkinter.DISABLED)
outputArea.pack(side=tkinter.BOTTOM)
outputArea.place(x=10, y=180)

mainWindow.mainloop()