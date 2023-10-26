# DemoForm.py

import typing
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

form_class=uic.loadUiType("DemoForm.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면 보여주기")        
        self.label_2.setText("Test")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    DemoForm = DemoForm()
    DemoForm.show()
    app.exec_()