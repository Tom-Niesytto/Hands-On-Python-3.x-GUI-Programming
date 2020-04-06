'''
Created on Mar 7, 2019
@author: Burkhard A. Meier
'''


# class inheriting from QWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget 
 
#QWidget class is the base class of all user interface objects.
class GUI(QWidget):                 # inherit from QWidget
    def __init__(self): 
        super().__init__()          # initialize super class, which creates the Window - need to do it explicitly here 
        self.initUI()               # refer to Window as 'self'
          
    def initUI(self):
        #print(self.windowTitle())
        self.setWindowTitle('PyQt5 GUI')    # call method
        #print(self.windowTitle())
        #This property holds the window title (caption)
        #This property only makes sense for top-level widgets, such as windows and dialogs.
        #If no caption has been set, the title is based of the windowFilePath.
        #If neither of these is set, then the title is an empty string.
 
 
if __name__ == '__main__':     
    app = QApplication(sys.argv)        # create Application (why do we need it?)    
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application (event loop)
                                        # Note: Enters the main event loop and waits until exit() is called,
                                        #       then returns the value that was set to exit() (which is 0 if exit() is called via quit()).


















