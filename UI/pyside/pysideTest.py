import sys
from PySide.QtGui import *
 

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("PySide Test")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    app.exec_()
    sys.exit(0)