# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:19:29 2022

@author: Hanson
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSize, Qt, pyqtSlot


class Login(QWidget):

    def __init__(self):
        super().__init__()

        layout = QFormLayout()
        
        self.nmbr = 0
        self.displayText = QLabel(f'Nilai Antrian: {self.nmbr}')
        self.btnAdd = self.kompenenBtn('Tambah', self.submitAdd)
        self.btnSubtract = self.kompenenBtn('Kurang', self.submitSubtract)
        self.btnClear = self.kompenenBtn('Clear', self.clearData)
        
        layout.addRow(self.displayText)
        layout.addRow(self.btnAdd)
        layout.addRow(self.btnSubtract)
        layout.addRow(self.btnClear)
        
        self.setLayout(layout)
        self.setWindowTitle('Addition and Subtraction')
        self.setFixedSize(QSize(400, 300))
        
    def kompenenBtn(self, text, connectFunc):
        btn = QPushButton(text)
        btn.clicked.connect(connectFunc)
        return btn
    
    def submitAdd(self):
        self.nmbr = self.nmbr + 1
        self.displayText.setText(f'Nilai Antrian: {self.nmbr}')

    def submitSubtract(self):
        if (self.nmbr > 0):
            self.nmbr = self.nmbr - 1
            self.displayText.setText(f'Nilai Antrian: {self.nmbr}')
        
    def clearData(self):
        self.nmbr = 0
        self.displayText.setText(f'Nilai Antrian: {self.nmbr}')
        

app = QApplication(sys.argv)
login = Login()
login.show()
app.exec_()