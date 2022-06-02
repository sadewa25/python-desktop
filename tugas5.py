# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:20:51 2022

@author: Hanson
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt, pyqtSlot

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Addition")
        self.setFixedSize(QSize(200, 100))
        
        self.nmbr = '0'
        self.label = QLabel(self.nmbr)
        self.label.setAlignment(Qt.AlignCenter)

        self.input1 = QLineEdit()
        self.input1.textChanged.connect(self.onTextChanged)
        
        self.input2 = QLineEdit()
        self.input2.textChanged.connect(self.onTextChanged)

        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def onTextChanged(self, text) :
        if (text == ''): 
            self.label.setText('0')
        else:
            nmbr1 = int(self.input1.text())
            nmbr2 = int(self.input2.text())
        
            self.nmbr = nmbr1 + nmbr2
            self.label.setText(f'{self.nmbr}')
        
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()