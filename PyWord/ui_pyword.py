# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pywordadTGzC.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionBold = QAction(MainWindow)
        self.actionBold.setObjectName(u"actionBold")
        self.actionItalic = QAction(MainWindow)
        self.actionItalic.setObjectName(u"actionItalic")
        self.actionUnderline = QAction(MainWindow)
        self.actionUnderline.setObjectName(u"actionUnderline")
        self.actionDefault = QAction(MainWindow)
        self.actionDefault.setObjectName(u"actionDefault")
        self.actionSpelling = QAction(MainWindow)
        self.actionSpelling.setObjectName(u"actionSpelling")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.font_size_button = QSpinBox(self.centralwidget)
        self.font_size_button.setObjectName(u"font_size_button")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.font_size_button.setFont(font)
        self.font_size_button.setMinimum(5)

        self.gridLayout.addWidget(self.font_size_button, 3, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 7, 1, 1)

        self.default_button = QPushButton(self.centralwidget)
        self.default_button.setObjectName(u"default_button")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.default_button.setFont(font1)
        self.default_button.setStyleSheet(u"border-radius:15px; background-color: white;border: 1px solid grey;")

        self.gridLayout.addWidget(self.default_button, 3, 4, 1, 1)

        self.bold_button = QPushButton(self.centralwidget)
        self.bold_button.setObjectName(u"bold_button")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.bold_button.setFont(font2)
        self.bold_button.setStyleSheet(u"border-radius:15px; background-color: white;border: 1px solid grey;")

        self.gridLayout.addWidget(self.bold_button, 3, 1, 1, 1)

        self.italic_button = QPushButton(self.centralwidget)
        self.italic_button.setObjectName(u"italic_button")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setItalic(True)
        self.italic_button.setFont(font3)
        self.italic_button.setStyleSheet(u"border-radius:15px; background-color: white;border: 1px solid grey;")

        self.gridLayout.addWidget(self.italic_button, 3, 2, 1, 1)

        self.underline_button = QPushButton(self.centralwidget)
        self.underline_button.setObjectName(u"underline_button")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setUnderline(True)
        self.underline_button.setFont(font4)
        self.underline_button.setStyleSheet(u"border-radius:15px; background-color: white;border: 1px solid grey;")

        self.gridLayout.addWidget(self.underline_button, 3, 3, 1, 1)

        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(20)
        self.title.setFont(font5)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 2, 1, 1, 8)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font1)

        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionBold)
        self.menuEdit.addAction(self.actionItalic)
        self.menuEdit.addAction(self.actionUnderline)
        self.menuEdit.addAction(self.actionDefault)
        self.menuTools.addAction(self.actionSpelling)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionBold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.actionItalic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.actionUnderline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.actionDefault.setText(QCoreApplication.translate("MainWindow", u"Default ", None))
        self.actionSpelling.setText(QCoreApplication.translate("MainWindow", u"Spelling", None))
        self.default_button.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.bold_button.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.italic_button.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.underline_button.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"PyWord", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

