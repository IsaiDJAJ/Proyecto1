# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proyect.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_AppendText = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AppendText.setGeometry(QtCore.QRect(540, 370, 101, 25))
        self.pushButton_AppendText.setObjectName("pushButton_AppendText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 481, 361))
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 10, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(530, 40, 251, 101))
        self.textEdit.setObjectName("textEdit")
        self.pushButtonColor = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonColor.setGeometry(QtCore.QRect(540, 270, 89, 25))
        self.pushButtonColor.setObjectName("pushButtonColor")
        self.label_Text = QtWidgets.QLabel(self.centralwidget)
        self.label_Text.setGeometry(QtCore.QRect(616, 10, 81, 20))
        self.label_Text.setObjectName("label_Text")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(540, 170, 226, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_SelectFont = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectFont.setGeometry(QtCore.QRect(540, 140, 211, 31))
        self.label_SelectFont.setObjectName("label_SelectFont")
        self.label_Size = QtWidgets.QLabel(self.centralwidget)
        self.label_Size.setGeometry(QtCore.QRect(540, 210, 67, 17))
        self.label_Size.setObjectName("label_Size")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(540, 230, 48, 26))
        self.spinBox.setObjectName("spinBox")
        self.l_TD = QtWidgets.QLabel(self.centralwidget)
        self.l_TD.setGeometry(QtCore.QRect(170, 70, 171, 91))
        self.l_TD.setMouseTracking(True)
        self.l_TD.setAutoFillBackground(False)
        self.l_TD.setStyleSheet("")
        self.l_TD.setFrameShape(QtWidgets.QFrame.Box)
        self.l_TD.setText("")
        self.l_TD.setScaledContents(True)
        self.l_TD.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l_TD.setWordWrap(False)
        self.l_TD.setObjectName("l_TD")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 230, 41, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 230, 41, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 230, 41, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(626, 200, 131, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionImage = QtWidgets.QAction(MainWindow)
        self.actionImage.setObjectName("actionImage")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionCtrl_N = QtWidgets.QAction(MainWindow)
        self.actionCtrl_N.setObjectName("actionCtrl_N")
        self.actionNew_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionText = QtWidgets.QAction(MainWindow)
        self.actionText.setObjectName("actionText")
        self.menuFile.addAction(self.actionNew_2)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_AppendText.setText(_translate("MainWindow", "Append text"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonColor.setText(_translate("MainWindow", "Color"))
        self.label_Text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Text</span></p></body></html>"))
        self.label_SelectFont.setText(_translate("MainWindow", "Select Font"))
        self.label_Size.setText(_translate("MainWindow", "Size"))
        self.pushButton.setText(_translate("MainWindow", "D"))
        self.pushButton_2.setText(_translate("MainWindow", "C"))
        self.pushButton_3.setText(_translate("MainWindow", "I"))
        self.label_2.setText(_translate("MainWindow", "Text aligment"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As.."))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All.."))
        self.actionCtrl_N.setText(_translate("MainWindow", "Ctrl N"))
        self.actionNew_2.setText(_translate("MainWindow", "New"))
        self.actionNew_2.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionText.setText(_translate("MainWindow", "Text"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
