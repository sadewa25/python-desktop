# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:42:13 2022

@author: SadewaWicak
"""

# daftarBuku = ['Sosiologi', 'Matematika', 'IPA']
# print(daftarBuku[2])


# wargaRt = {"nama": "Bejo", "umur": "30"}
# print(wargaRt['nama'])


import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLineEdit

# Subclass QMainWindow to customize your application's main window


class MainWindow(QWidget):

    def __init__(self, layout):
        super().__init__()

        self.setWindowTitle("Layout Manager")
        self.setFixedSize(QSize(800, 700))

        if layout == 'horizontal':
            self.setLayout(self.horizontalLayout())
        elif layout == 'vertical':
            self.setLayout(self.verticalLayout())

    def horizontalLayout(self):
        layout = QHBoxLayout()
        layout.addWidget(QPushButton('Left'))
        layout.addWidget(QPushButton('Center'))
        layout.addWidget(QPushButton('Right'))
        return layout

    def verticalLayout(self):
        layout = QVBoxLayout()
        panjang = QLineEdit()
        panjang.setPlaceholderText('Panjang')
        lebar = QLineEdit()
        lebar.setPlaceholderText('Lebar')
        layout.addWidget(panjang)
        layout.addWidget(lebar)
        layout.addWidget(QPushButton('Hitung'))
        return layout


app = QApplication(sys.argv)

# window = MainWindow('form')
window = MainWindow('vertical')

window.show()

app.exec()
