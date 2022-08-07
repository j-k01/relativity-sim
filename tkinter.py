import tkinter as tk

from os import path
from os import listdir
from PIL import Image, ImageTk

        
class Annotator():
    def __init__( self, window):
        #tk.Frame.__init__(self, window)
        self.window = window
        self.window.configure(background = 'grey')\
            
        self._createWidgets()
        self._createBindings()
        self._createLayout()

        
    def doNothing(self):
        '''
        Do-nothing "command" for hidden buttons associated with a key-press.
        '''
        pass
    
    
    def _createBindings(self):
        self.canvas.bind( "<Button-1>", self.clickCanvas)
        self.canvas.bind( "<ButtonRelease-1>", self.releaseCanvas)     


    def _createWidgets(self):
        self.canvas = tk.Canvas(self.window, width = 640, height = 512,
                                  bg = "white",borderwidth=0, highlightthickness=0) 
        
          
    def _createLayout(self):
          self.window.grid_columnconfigure(0, minsize=30)
          self.window.grid_rowconfigure(0, minsize=30)
    
          self.canvas.grid(row=1, column=1, columnspan = 10,rowspan = 10)
          
    def clickCanvas(self, event):
        self.cursorx = self.canvas.canvasx(event.x)
        self.cursory = self.canvas.canvasy(event.y) 
        
        
    def releaseCanvas(self, event):
       print(self.cursorx)
       #self.canvas.unbind("<Motion>")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry( "1000x600" )
    root.title('realtivity')
    ann = Annotator(root)
    root.mainloop()