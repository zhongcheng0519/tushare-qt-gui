# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetPriceDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(233, 196)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.doubleSpinBoxBoughtPrice = QDoubleSpinBox(Dialog)
        self.doubleSpinBoxBoughtPrice.setObjectName(u"doubleSpinBoxBoughtPrice")

        self.gridLayout.addWidget(self.doubleSpinBoxBoughtPrice, 2, 1, 1, 1)

        self.doubleSpinBoxLowPEThresh = QDoubleSpinBox(Dialog)
        self.doubleSpinBoxLowPEThresh.setObjectName(u"doubleSpinBoxLowPEThresh")

        self.gridLayout.addWidget(self.doubleSpinBoxLowPEThresh, 4, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.doubleSpinBoxHighPEThresh = QDoubleSpinBox(Dialog)
        self.doubleSpinBoxHighPEThresh.setObjectName(u"doubleSpinBoxHighPEThresh")

        self.gridLayout.addWidget(self.doubleSpinBoxHighPEThresh, 5, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.labelStockName = QLabel(Dialog)
        self.labelStockName.setObjectName(u"labelStockName")

        self.gridLayout.addWidget(self.labelStockName, 0, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Set Price", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Stock:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Bought Price:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Low PE Thresh:", None))
        self.labelStockName.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"High PE Thresh:", None))
    # retranslateUi

