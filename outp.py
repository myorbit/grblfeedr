# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Sep 24 23:40:46 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 359)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMouseTracking(True)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(3, 3, 750, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Desktop/git/grblfeedr/grblfeeder.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.connectButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.connectButton.setMinimumSize(QtCore.QSize(0, 40))
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_4.addWidget(self.connectButton)
        self.disconnectButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.disconnectButton.setEnabled(False)
        self.disconnectButton.setMinimumSize(QtCore.QSize(0, 40))
        self.disconnectButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout_4.addWidget(self.disconnectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.nextScreen = QtGui.QPushButton(self.verticalLayoutWidget)
        self.nextScreen.setObjectName("nextScreen")
        self.horizontalLayout_3.addWidget(self.nextScreen)
        self.exitButton2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.exitButton2.setObjectName("exitButton2")
        self.horizontalLayout_3.addWidget(self.exitButton2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(440, 10, 301, 281))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 481, 310))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layout2 = QtGui.QWidget(self.splitter)
        self.layout2.setObjectName("layout2")
        self.topHoriz = QtGui.QHBoxLayout(self.layout2)
        self.topHoriz.setContentsMargins(0, 0, 0, 0)
        self.topHoriz.setObjectName("topHoriz")
        self.termWindow = QtGui.QTextEdit(self.layout2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.termWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Terminal_Hex")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.termWindow.setFont(font)
        self.termWindow.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.termWindow.setMouseTracking(True)
        self.termWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.termWindow.setAcceptDrops(True)
        self.termWindow.setFrameShadow(QtGui.QFrame.Plain)
        self.termWindow.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.termWindow.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.termWindow.setReadOnly(True)
        self.termWindow.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.termWindow.setObjectName("termWindow")
        self.topHoriz.addWidget(self.termWindow)
        self.controlVert = QtGui.QVBoxLayout()
        self.controlVert.setSpacing(3)
        self.controlVert.setObjectName("controlVert")
        self.loadButton = QtGui.QPushButton(self.layout2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loadButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.loadButton.setFlat(False)
        self.loadButton.setObjectName("loadButton")
        self.controlVert.addWidget(self.loadButton)
        self.sendOne = QtGui.QPushButton(self.layout2)
        self.sendOne.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sendOne.setObjectName("sendOne")
        self.controlVert.addWidget(self.sendOne)
        self.sendCont = QtGui.QPushButton(self.layout2)
        self.sendCont.setMinimumSize(QtCore.QSize(90, 0))
        self.sendCont.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sendCont.setObjectName("sendCont")
        self.controlVert.addWidget(self.sendCont)
        self.sendStop = QtGui.QPushButton(self.layout2)
        self.sendStop.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sendStop.setFlat(False)
        self.sendStop.setObjectName("sendStop")
        self.controlVert.addWidget(self.sendStop)
        self.clearButton = QtGui.QPushButton(self.layout2)
        self.clearButton.setObjectName("clearButton")
        self.controlVert.addWidget(self.clearButton)
        self.clearTerm = QtGui.QPushButton(self.layout2)
        self.clearTerm.setObjectName("clearTerm")
        self.controlVert.addWidget(self.clearTerm)
        self.topHoriz.addLayout(self.controlVert)
        self.termLine = QtGui.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Terminal_Hex")
        font.setPointSize(10)
        self.termLine.setFont(font)
        self.termLine.setObjectName("termLine")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.bottomHoriz = QtGui.QHBoxLayout(self.layoutWidget)
        self.bottomHoriz.setContentsMargins(0, 0, 0, 0)
        self.bottomHoriz.setObjectName("bottomHoriz")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottomHoriz.addItem(spacerItem)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Desktop/git/grblfeedr/grblfeeder.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.bottomHoriz.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottomHoriz.addItem(spacerItem1)
        self.exitButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QtCore.QSize(90, 0))
        self.exitButton.setMaximumSize(QtCore.QSize(100, 50))
        self.exitButton.setObjectName("exitButton")
        self.bottomHoriz.addWidget(self.exitButton)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(490, 4, 250, 261))
        self.textEdit.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.currentProgress = QtGui.QProgressBar(self.tab)
        self.currentProgress.setGeometry(QtCore.QRect(490, 270, 251, 31))
        self.currentProgress.setProperty("value", 0)
        self.currentProgress.setAlignment(QtCore.Qt.AlignCenter)
        self.currentProgress.setOrientation(QtCore.Qt.Horizontal)
        self.currentProgress.setObjectName("currentProgress")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuQt = QtGui.QMenu(self.menuBar)
        self.menuQt.setObjectName("menuQt")
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLoad_GCode = QtGui.QAction(MainWindow)
        self.actionLoad_GCode.setObjectName("actionLoad_GCode")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.menuQt.addAction(self.actionConnect)
        self.menuQt.addAction(self.actionLoad_GCode)
        self.menuQt.addAction(self.actionExit)
        self.menuBar.addAction(self.menuQt.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "grblfeedr", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Serial Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Baud Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnectButton.setText(QtGui.QApplication.translate("MainWindow", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.nextScreen.setText(QtGui.QApplication.translate("MainWindow", "Next Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton2.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">grblfeeder</span><span style=\" font-size:12pt;\">, a GUI serial terminal for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sending commands to </span><span style=\" font-size:12pt; font-weight:600;\">GRBL</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Uses </span><span style=\" font-size:12pt; font-weight:600;\">Python</span><span style=\" font-size:12pt;\">, </span><span style=\" font-size:12pt; font-weight:600;\">PySide</span><span style=\" font-size:12pt;\">, </span><span style=\" font-size:12pt; font-weight:600;\">Qt</span><span style=\" font-size:12pt;\">, and </span><span style=\" font-size:12pt; font-weight:600;\">PySerial</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Comments to </span><span style=\" font-size:12pt; font-weight:600;\">timkrins@gmail.com</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.termWindow.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Terminal_Hex\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">termWindow</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("MainWindow", "Load File", None, QtGui.QApplication.UnicodeUTF8))
        self.sendOne.setText(QtGui.QApplication.translate("MainWindow", "Send One Line", None, QtGui.QApplication.UnicodeUTF8))
        self.sendCont.setText(QtGui.QApplication.translate("MainWindow", "Send Continous", None, QtGui.QApplication.UnicodeUTF8))
        self.sendStop.setText(QtGui.QApplication.translate("MainWindow", "Stop Sending", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "Clear Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.clearTerm.setText(QtGui.QApplication.translate("MainWindow", "Clear Terminal", None, QtGui.QApplication.UnicodeUTF8))
        self.termLine.setText(QtGui.QApplication.translate("MainWindow", "Enter Command", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.currentProgress.setFormat(QtGui.QApplication.translate("MainWindow", "Queue Progress: %p%", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Feeder", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQt.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_GCode.setText(QtGui.QApplication.translate("MainWindow", "Load GCode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))

