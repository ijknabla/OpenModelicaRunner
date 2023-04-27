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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHeaderView,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTreeWidget,
    QTreeWidgetItem, QWidget)

from omrun.widget.modelbrowser import ModelBrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.modelBroswerAction = QAction(MainWindow)
        self.modelBroswerAction.setObjectName(u"modelBroswerAction")
        self.modelBroswerAction.setCheckable(True)
        self.modelBroswerAction.setChecked(True)
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
        self.viewMenu = QMenu(self.menubar)
        self.viewMenu.setObjectName(u"viewMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.modelBrowserDockWidget = QDockWidget(MainWindow)
        self.modelBrowserDockWidget.setObjectName(u"modelBrowserDockWidget")
        self.modelBrowser = ModelBrowser()
        self.modelBrowser.setObjectName(u"modelBrowser")
        self.modelBrowserDockWidget.setWidget(self.modelBrowser)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.modelBrowserDockWidget)

        self.menubar.addAction(self.viewMenu.menuAction())
        self.viewMenu.addAction(self.modelBroswerAction)

        self.retranslateUi(MainWindow)
        self.modelBroswerAction.triggered["bool"].connect(self.modelBrowserDockWidget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.modelBroswerAction.setText(QCoreApplication.translate("MainWindow", u"&Model Broswer", None))
        ___qtreewidgetitem = self.modelTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u00a0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"model", None));
        self.viewMenu.setTitle(QCoreApplication.translate("MainWindow", u"&View", None))
    # retranslateUi

