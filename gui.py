#Display Calendar and call methodes in model file


from importlib.resources import path
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

#get Filename of calendar and pass it
def getFilename() -> path:
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return(filename)