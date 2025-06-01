import tkinter as tk
from tkinter.filedialog import askopenfilename
import PhotoReaderGUI

def browseFilesCommand():
    fn = askopenfilename()
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.NORMAL)
    PhotoReaderGUI.filepathEntryWidget.insert(tk.END, fn)
    PhotoReaderGUI.filepathEntryWidget.config(state=tk.DISABLED)