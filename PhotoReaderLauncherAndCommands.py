import tkinter as tk
from tkinter import PhotoImage, Label
from tkinter.filedialog import askopenfilename

from PIL import Image

import PhotoReaderGUI
import pytesseract

image = ""
imageText = ""

def browseFilesCommand():
    fn = askopenfilename()
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.filepathEntryWidget.insert(tk.END, fn)
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)

def clearImageAndTextCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.filepathEntryWidget.delete(0, tk.END)
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.delete(1.0, tk.END)
    PhotoReaderGUI.outputArea.config(image="", state=tk.DISABLED)

def analyzeImageTextCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    inserted_image = PhotoImage(file=PhotoReaderGUI.filepathEntryWidget.get())
    imageLabel = tk.Label(PhotoReaderGUI.mainWindow, image=inserted_image, width=PhotoReaderGUI.outputArea.winfo_width(), height=PhotoReaderGUI.outputArea.winfo_height())
    imageLabel.place(x=6, y=180)
    PhotoReaderGUI.outputArea.insert(tk.END, imageLabel).pack()
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)

def leftArrowCommand():
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    # finish left arrow button functionality here.
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)

def rightArrowCommand():
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    # finish right arrow button functionality here.
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)