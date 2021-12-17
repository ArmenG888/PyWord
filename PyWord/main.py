import sys,re
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,QRegExp)
from PySide2.QtGui import (QBrush, QColor, QSyntaxHighlighter,QConicalGradient,QTextCharFormat, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_pyword import Ui_MainWindow

class main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.font = QFont()
        self.font.setFamily(u"Segoe UI")
        self.font.setPointSize(12)
        self.filename = "None"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setWindowTitle('PyWord')
        self.setup_menus()
        self.ui.bold_button.clicked.connect(self.bold)
        self.ui.default_button.clicked.connect(self.default)
        self.show()
    def setup_menus(self):
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionSave.setShortcut("Ctrl+S")
        self.ui.actionSave_As.triggered.connect(self.save_as)
        self.ui.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionNew.setShortcut("Ctrl+N")
    def save(self):
        cursor = self.ui.textEdit.textCursor()
        print ("Selection start: %d end: %d" % 
           (cursor.selectionStart(), cursor.selectionEnd()))
        if self.filename == "None":
            self.save_as()
        with open(self.filename, "w") as w:
            w.write(self.ui.textEdit.toPlainText())
        return
    def save_as(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            self.filename = dialog.selectedFiles()
        with open(self.filename, "w") as w:
            w.write(self.ui.textEdit.toPlainText())
    def new(self):
        self.setWindowTitle("PyWord Untitled")
        self.ui.textEdit.setText("")
    def license(self):
        with open("License","r") as r:
            r = r.read()
        self.ui.textEdit.setText(r)
        cursor = self.ui.textEdit.textCursor()
        print ("Selection start: %d end: %d" % 
           (cursor.selectionStart(), cursor.selectionEnd()))
    def open(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_():
            self.filename = dialog.selectedFiles()[0]
            print(self.filename)
        with open(self.filename, "r") as r:
            file_content = r.read()
        self.ui.textEdit.setText(file_content)
        self.setWindowTitle("PyWord " + self.filename)
    def default(self):
        self.ui.textEdit.setFontWeight(QFont.Normal)
    def bold(self):
        self.ui.textEdit.setFontWeight(QFont.Bold)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())

