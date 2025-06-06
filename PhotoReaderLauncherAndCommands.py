# Name: Rusho Binnabi
# Date: 6/6/2025
# Project: PhotoReader - Launcher and Commands
# Contact Information: RushoBinnabi123@yahoo.com

import tkinter as tk
from tkinter.filedialog import askopenfilename

from PIL import Image

import PhotoReaderGUI
import pytesseract

# this PhotoReaderLauncherAndCommands file has the code for launching the application and all the associated commands
# when the GUI is interacted with.

image = "" # this image variable has the filepath for the image that is being processed.
imageText = "" # this imageText variable has the text that is generated from image.

# this browseFilesCommand() function gets the image files that will be used and processed by the application
# when the appropriate button is clicked.

def browseFilesCommand():
    fn = askopenfilename()
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.filepathEntryWidget.insert(tk.END, fn)
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)

# this clearCommand() function will clear the application screen when the appropriate button is clicked.

def clearCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.filepathEntryWidget.delete(0, tk.END)
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.delete(1.0, tk.END)
    PhotoReaderGUI.outputArea.config(image="")
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)

# this analyzeImageCommand() will analyze the text and extract the text from them and display it on the GUI
# when the appropriate button is clicked.

def analyzeImageCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    image = Image.open(PhotoReaderGUI.filepathEntryWidget.get())
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    imageText = pytesseract.image_to_string(image)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.insert(tk.END, imageText)
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)