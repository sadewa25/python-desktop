# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:42:13 2022

@author: SadewaWicak
"""

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QFormLayout, QLineEdit

# Subclass QMainWindow to customize your application's main window


class MainWindow(QWidget):

    def __init__(self, layout):
        super().__init__()

        self.setWindowTitle("Kalkulator Luas")
        self.setFixedSize(QSize(400, 100))
        
        if layout == 'vertical':
            self.setLayout(self.verticalLayout())
        elif layout == 'form':
            self.setLayout(self.formLayout())

    def verticalLayout(self):
        layout = QVBoxLayout()
        return layout
    
    def formLayout(self):
        layout = QFormLayout()
        layout.addRow('Panjang:', QLineEdit())
        layout.addRow('Lebar:', QLineEdit())
        layout.addWidget(QPushButton('Hitung'))
        return layout 
    

app = QApplication(sys.argv)

window = MainWindow('form')
# window = MainWindow('vertical')

window.show()

app.exec()
