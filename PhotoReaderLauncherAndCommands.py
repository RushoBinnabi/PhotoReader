import tkinter as tk
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

def clearCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.filepathEntryWidget.delete(0, tk.END)
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.delete(1.0, tk.END)
    PhotoReaderGUI.outputArea.config(image="")
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)

def analyzeImageCommand():
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    image = Image.open(PhotoReaderGUI.filepathEntryWidget.get())
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)
    imageText = pytesseract.image_to_string(image)
    PhotoReaderGUI.outputArea.config(state=tk.NORMAL)
    PhotoReaderGUI.outputArea.insert(tk.END, imageText)
    PhotoReaderGUI.outputArea.config(state=tk.DISABLED)