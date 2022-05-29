# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:58:20 2022

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

        self.dataPanjang = self.komponenEditText('Panjang')

        self.dataLebar = self.komponenEditText("Lebar")

        self.btnCount = self.kompenenBtn('Hitung', self.submitCount)
        
        self.displayText = QLabel()
        
        self.btnClear = self.kompenenBtn('Clear', self.clearData)
        
        layout.addRow(self.dataPanjang)
        layout.addRow(self.dataLebar)
        layout.addRow(self.btnCount)
        layout.addRow(self.btnClear)
        layout.addRow(self.displayText)

        self.setLayout(layout)
        self.setWindowTitle("Kalkulator Luas Persegi Panjang")
        self.setFixedSize(QSize(600, 200))

    def submitCount(self):
        calculate = int(self.dataPanjang.text()) * int(self.dataLebar.text())
        self.displayText.setText(str(calculate))
        print(str(calculate))
        
    def clearData(self):
        self.dataPanjang.clear()
        self.dataLebar.clear()
        self.displayText.clear()
        
    def komponenEditText(self, text):
        edit = QLineEdit()
        edit.setPlaceholderText(text)
        return edit
    
    def kompenenBtn(self, text, connectFunc):
        btn = QPushButton(text)
        btn.clicked.connect(connectFunc)
        return btn


app = QApplication(sys.argv)
login = Login()
login.show()
app.exec_()