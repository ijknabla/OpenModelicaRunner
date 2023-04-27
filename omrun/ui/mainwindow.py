# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_Model_Broswer = QAction(MainWindow)
        self.action_Model_Broswer.setObjectName(u"action_Model_Broswer")
        self.action_Model_Broswer.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralLayout = QGridLayout(self.centralwidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.modelTree = QTreeWidget(self.centralwidget)
        self.modelTree.setObjectName(u"modelTree")

        self.centralLayout.addWidget(self.modelTree, 0, 0, 1, 1)

        self.processWidget = QListWidget(self.centralwidget)
        self.processWidget.setObjectName(u"processWidget")

        self.centralLayout.addWidget(self.processWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        self.menu_View = QMenu(self.menubar)
        self.menu_View.setObjectName(u"menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_View.menuAction())
        self.menu_View.addAction(self.action_Model_Broswer)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Model_Broswer.setText(QCoreApplication.translate("MainWindow", u"&Model Broswer", None))
        ___qtreewidgetitem = self.modelTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u00a0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"model", None));
        self.menu_View.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
    # retranslateUi

