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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_ModelBrowser(object):
    def setupUi(self, ModelBrowser):
        if not ModelBrowser.objectName():
            ModelBrowser.setObjectName(u"ModelBrowser")
        ModelBrowser.resize(400, 300)
        self.gridLayout = QGridLayout(ModelBrowser)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(ModelBrowser)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)


        self.retranslateUi(ModelBrowser)

        QMetaObject.connectSlotsByName(ModelBrowser)
    # setupUi

    def retranslateUi(self, ModelBrowser):
        ModelBrowser.setWindowTitle(QCoreApplication.translate("ModelBrowser", u"ModelBrowser", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ModelBrowser", u"\u00a0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ModelBrowser", u"model", None));
    # retranslateUi

