# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:49:14 2022

@author: Hanson
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Polindrome Check")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.onTextChanged)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def onTextChanged(self, text):
        if (text == text[::-1]):
            self.label.setText(text)
        else:
            self.label.clear()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()