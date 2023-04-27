# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelbrowser.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ModelBrowser(object):
    def setupUi(self, ModelBrowser):
        if not ModelBrowser.objectName():
            ModelBrowser.setObjectName(u"ModelBrowser")
        ModelBrowser.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ModelBrowser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.workDirectoryLabel = QLabel(ModelBrowser)
        self.workDirectoryLabel.setObjectName(u"workDirectoryLabel")

        self.horizontalLayout.addWidget(self.workDirectoryLabel)

        self.reloadPushButton = QPushButton(ModelBrowser)
        self.reloadPushButton.setObjectName(u"reloadPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reloadPushButton.sizePolicy().hasHeightForWidth())
        self.reloadPushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.reloadPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.treeWidget = QTreeWidget(ModelBrowser)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)


        self.retranslateUi(ModelBrowser)

        QMetaObject.connectSlotsByName(ModelBrowser)
    # setupUi

    def retranslateUi(self, ModelBrowser):
        ModelBrowser.setWindowTitle(QCoreApplication.translate("ModelBrowser", u"ModelBrowser", None))
        self.workDirectoryLabel.setText(QCoreApplication.translate("ModelBrowser", u"/path/to/OMEdit", None))
        self.reloadPushButton.setText(QCoreApplication.translate("ModelBrowser", u"reload", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ModelBrowser", u"\u00a0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ModelBrowser", u"model", None));
    # retranslateUi

