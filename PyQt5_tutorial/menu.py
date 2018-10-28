#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
    QPushButton, QAction, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menu example')
        self.setGeometry(300, 300, 300, 200)

        # main menu
        mainMenu = self.menuBar()

        # file menu
        fileMenu = mainMenu.addMenu('File')

        openButton = QAction('Open', self)
        openButton.triggered.connect(self.onOpenFile)
        fileMenu.addAction(openButton)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # help menu
        helpMenu = mainMenu.addMenu('Help')
        aboutButton = QAction('About', self)
        aboutButton.triggered.connect(self.onAbout)
        helpMenu.addAction(aboutButton)

        aboutQtButton = QAction('AboutQt', self)
        aboutQtButton.triggered.connect(self.onAboutQt)
        helpMenu.addAction(aboutQtButton)

        self.show()

    def onOpenFile(self):
        QMessageBox.information(self, 'Info', 'Open file ...')

    def onAbout(self):
        QMessageBox.about(self, 'About', 'This is about message.')

    def onAboutQt(self):
        QMessageBox.aboutQt(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
