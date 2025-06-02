import tkinter as tk
from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

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
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)

def analyzeImageTextCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    inserted_image = Image.open(PhotoReaderGUI.filepathEntryWidget.get())
    imageText = pytesseract.image_to_string(inserted_image)
    # finish functionality here.
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)

def leftArrowCommand():
    print()

def rightArrowCommand():
    print()