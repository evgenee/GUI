import tkinter as tk
import tkinter.tix as tix
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image
#from os import Exception
import os


included_extensions = ['jpg', 'bmp', 'png', 'gif', 'tiff']

class ImageConverterGui(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.path_text = tk.StringVar()
        self.grid()
        self.initUI()

    def initUI(self):
        self.master.title("Image Converter")
        self.lblPath = tk.Label(self, text='Image directory path:')
        self.lblPath.grid(row=0, column=0, sticky='w')
        self.entrPath = tk.Entry(self, textvariable=self.path_text, width=80)
        self.entrPath.grid(row=0, column=1, columnspan=3, sticky='we', padx=5)

        self.btnBrowseDir = tk.Button(self, text='Browse...', command=lambda:self.getDir())
        self.btnBrowseDir.grid(row=0, column=4, sticky='w')

        '''
        self.listConvertFormats = tk.Listbox(self, width=80)
        pos = 0
        for ext in included_extensions: # add to listbox
            self.listConvertFormats.insert(pos, ext) # or insert(END,label)
            pos += 1
        self.listConvertFormats.config(yscrollcommand=sbar.set)
        self.listConvertFormats.grid(row=1, column=1, columnspan=3, sticky='we', padx=5)

        self.btnConvert = tk.Button(self, text='Convert', command=lambda:self.convertImageFormat(self.path_text, destinationFormat))
        self.btnConvert.grid(row=1, column=4, sticky='w')
        '''
        self.txtLog = tk.Text(self)
        self.txtLog.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

    def getDir(self):
        dirname = tk.filedialog.askdirectory(title="Select A Folder",initialdir=self.path_text)
        if dirname:
            self.path_text.set(dirname)
'''
    def convertImageFormat(self, dirname, destinationFormat):
        global included_extensions
        filelist = [fn for fn in os.listdir(dirname)
              if fn.endswith(ext) for ext in included_extensions]
        for infile in filelist:
            outfile = os.path.splitext(infile)[0] + destinationFormat
            if infile != outfile:
             try:
                Image.open(infile).save(outfile)
                self.txtLog.insert(END, infile " is converted to " outfile "/n")
             except IOError:
                self.txtLog.insert(END, "something wrong in convertion of " infile " to " outfile "/n")
'''

def main():
    root = tk.Tk()
    #root.geometry("600x450+250+150")
    app = ImageConverterGui(master=root)
    app.mainloop()
if __name__ == '__main__':
    main()