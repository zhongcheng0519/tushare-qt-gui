# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BasicPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1643, 822)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeWidget = QTreeWidget(Form)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QSize(500, 0))

        self.horizontalLayout_2.addWidget(self.treeWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dateEditFrom = QDateEdit(Form)
        self.dateEditFrom.setObjectName(u"dateEditFrom")

        self.horizontalLayout.addWidget(self.dateEditFrom)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.dateEditTo = QDateEdit(Form)
        self.dateEditTo.setObjectName(u"dateEditTo")

        self.horizontalLayout.addWidget(self.dateEditTo)

        self.pushButtonLastMonth = QPushButton(Form)
        self.pushButtonLastMonth.setObjectName(u"pushButtonLastMonth")

        self.horizontalLayout.addWidget(self.pushButtonLastMonth)

        self.pushButtonLastThreeMonths = QPushButton(Form)
        self.pushButtonLastThreeMonths.setObjectName(u"pushButtonLastThreeMonths")

        self.horizontalLayout.addWidget(self.pushButtonLastThreeMonths)

        self.pushButtonLastSixMonths = QPushButton(Form)
        self.pushButtonLastSixMonths.setObjectName(u"pushButtonLastSixMonths")

        self.horizontalLayout.addWidget(self.pushButtonLastSixMonths)

        self.pushButtonLastYear = QPushButton(Form)
        self.pushButtonLastYear.setObjectName(u"pushButtonLastYear")

        self.horizontalLayout.addWidget(self.pushButtonLastYear)

        self.pushButtonLastTwoYears = QPushButton(Form)
        self.pushButtonLastTwoYears.setObjectName(u"pushButtonLastTwoYears")

        self.horizontalLayout.addWidget(self.pushButtonLastTwoYears)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.textEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonPECurve = QPushButton(Form)
        self.pushButtonPECurve.setObjectName(u"pushButtonPECurve")

        self.verticalLayout_2.addWidget(self.pushButtonPECurve)

        self.pushButtonPBCurve = QPushButton(Form)
        self.pushButtonPBCurve.setObjectName(u"pushButtonPBCurve")

        self.verticalLayout_2.addWidget(self.pushButtonPBCurve)

        self.pushButtonTurnoverRate = QPushButton(Form)
        self.pushButtonTurnoverRate.setObjectName(u"pushButtonTurnoverRate")

        self.verticalLayout_2.addWidget(self.pushButtonTurnoverRate)

        self.pushButtonDividend = QPushButton(Form)
        self.pushButtonDividend.setObjectName(u"pushButtonDividend")

        self.verticalLayout_2.addWidget(self.pushButtonDividend)

        self.pushButtonIncomeSheet = QPushButton(Form)
        self.pushButtonIncomeSheet.setObjectName(u"pushButtonIncomeSheet")

        self.verticalLayout_2.addWidget(self.pushButtonIncomeSheet)

        self.pushButtonBalanceSheet = QPushButton(Form)
        self.pushButtonBalanceSheet.setObjectName(u"pushButtonBalanceSheet")

        self.verticalLayout_2.addWidget(self.pushButtonBalanceSheet)

        self.pushButtonCashflowSheet = QPushButton(Form)
        self.pushButtonCashflowSheet.setObjectName(u"pushButtonCashflowSheet")

        self.verticalLayout_2.addWidget(self.pushButtonCashflowSheet)

        self.pushButtonSetPrice = QPushButton(Form)
        self.pushButtonSetPrice.setObjectName(u"pushButtonSetPrice")

        self.verticalLayout_2.addWidget(self.pushButtonSetPrice)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"\u8d2d\u5165\u4ef7\u683c", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"\u5f53\u524dPE", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"\u5f53\u524d\u4ef7\u683c", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"\u4ee3\u7801", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        self.label.setText(QCoreApplication.translate("Form", u"from:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"to:", None))
        self.pushButtonLastMonth.setText(QCoreApplication.translate("Form", u"\u6700\u8fd1\u4e00\u4e2a\u6708", None))
        self.pushButtonLastThreeMonths.setText(QCoreApplication.translate("Form", u"\u6700\u8fd1\u4e09\u4e2a\u6708", None))
        self.pushButtonLastSixMonths.setText(QCoreApplication.translate("Form", u"\u6700\u8fd1\u534a\u5e74", None))
        self.pushButtonLastYear.setText(QCoreApplication.translate("Form", u"\u6700\u8fd1\u4e00\u5e74", None))
        self.pushButtonLastTwoYears.setText(QCoreApplication.translate("Form", u"\u6700\u8fd1\u4e24\u5e74", None))
        self.pushButtonPECurve.setText(QCoreApplication.translate("Form", u"PE curve", None))
        self.pushButtonPBCurve.setText(QCoreApplication.translate("Form", u"PB curve", None))
        self.pushButtonTurnoverRate.setText(QCoreApplication.translate("Form", u"Turnover Rate", None))
        self.pushButtonDividend.setText(QCoreApplication.translate("Form", u"dividend", None))
        self.pushButtonIncomeSheet.setText(QCoreApplication.translate("Form", u"income sheet", None))
        self.pushButtonBalanceSheet.setText(QCoreApplication.translate("Form", u"balance sheet", None))
        self.pushButtonCashflowSheet.setText(QCoreApplication.translate("Form", u"cashflow sheet", None))
        self.pushButtonSetPrice.setText(QCoreApplication.translate("Form", u"set price", None))
    # retranslateUi

