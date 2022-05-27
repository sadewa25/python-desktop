# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:41:24 2022

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

        self.leUsername = self.komponenEditText('Masukkan Username')

        self.lePassword = self.komponenEditText("Masukkan Password", True)

        self.btnLogin = self.kompenenBtn('Submit', self.submitLogin)
        
        self.displayText = QLabel()
        
        self.btnClear = self.kompenenBtn('Clear', self.clearData)
        
        layout.addRow(self.leUsername)
        layout.addRow(self.lePassword)
        layout.addRow(self.btnLogin)
        layout.addRow(self.btnClear)
        layout.addRow(self.displayText)

        self.setLayout(layout)
        self.setWindowTitle("Login")
        self.setFixedSize(QSize(600, 200))

    def submitLogin(self):
        print(f'{self.leUsername.text()}---{self.lePassword.text()}')
        self.displayText.setText(f'{self.leUsername.text()}---{self.lePassword.text()}')
        
    def clearData(self):
        self.leUsername.clear()
        self.lePassword.clear()
        self.displayText.clear()
        
    def komponenEditText(self, text, isPassword=False):
        edit = QLineEdit()
        edit.setPlaceholderText(text)
        
        if(isPassword):
            edit.setEchoMode(QLineEdit.Password)
        
        return edit
    
    def kompenenBtn(self, text, connectFunc):
        btn = QPushButton(text)
        btn.clicked.connect(connectFunc)
        return btn


app = QApplication(sys.argv)
login = Login()
login.show()
app.exec_()