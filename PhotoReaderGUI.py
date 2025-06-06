# Name: Rusho Binnabi
# Date: 6/6/2025
# Project: PhotoReader - GUI
# Contact Information: RushoBinnabi123@yahoo.com

from tkinter import scrolledtext

import tkinter
import PhotoReaderLauncherAndCommands

# this PhotoReaderGUI file has the code needed for the GUI to function.

mainWindow = tkinter.Tk()
mainWindow.title("Photo Reader")
mainWindow.geometry("500x500")

filepathEntryWidget = tkinter.Entry(mainWindow, state=tkinter.DISABLED)
filepathEntryWidget.pack(side=tkinter.TOP, padx=15, pady=15)
filepathEntryWidget.place(x=117, y=38, width=170, height=22)

browseFilesButton = tkinter.Button(mainWindow, text="Browse Files", command=PhotoReaderLauncherAndCommands.browseFilesCommand)
browseFilesButton.pack(side=tkinter.TOP, padx=10, pady=50)
browseFilesButton.place(x=300, y=35)

analyzeImageText = tkinter.Button(mainWindow, text="Analyze Image", command=PhotoReaderLauncherAndCommands.analyzeImageCommand)
analyzeImageText.pack(side=tkinter.TOP, padx=10, pady=50)
analyzeImageText.place(x=165, y=78)

clearButton = tkinter.Button(mainWindow, text="Clear", command=PhotoReaderLauncherAndCommands.clearCommand)
clearButton.pack(side=tkinter.TOP, padx=10, pady=50)
clearButton.place(x=272, y=78)

outputArea = scrolledtext.ScrolledText(mainWindow, wrap=tkinter.WORD, width=58, height=22, state=tkinter.DISABLED)
outputArea.pack(side=tkinter.BOTTOM)
outputArea.place(x=10, y=130)

mainWindow.mainloop()