import pandas as pd
import toml
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from api.TuShare import TuShare
from GUI.basic.BasicPage import *
from GUI.basic.SetPriceDialogImp import SetPriceDialogImp
from utils.MyStockPrice import MyStockPrice


class BasicPageImp(QFrame):

    def __init__(self):
        super(BasicPageImp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.treeWidget.itemClicked.connect(self.onTreeWidgetItemClicked)
        self.tushare = TuShare()
        self.current_stock_code = None
        # set end date as today
        self.ui.dateEditTo.setDate(QDate().currentDate())
        # set default from date as 1 year ago
        self.ui.dateEditFrom.setDate(QDate().currentDate().addYears(-1))
        # ================= date selection ==========================
        self.ui.pushButtonLastMonth.clicked.connect(self.onPushButtonLastMonthClicked)
        self.ui.pushButtonLastThreeMonths.clicked.connect(self.onPushButtonLastThreeMonthsClicked)
        self.ui.pushButtonLastYear.clicked.connect(self.onPushButtonLastYearClicked)
        self.ui.pushButtonLastYear.clicked.connect(self.onPushButtonLastYearClicked)
        self.ui.pushButtonLastTwoYears.clicked.connect(self.onPushButtonLastTwoYearsClicked)
        # ==================  Command Buttons ===============================
        self.ui.pushButtonPECurve.clicked.connect(self.onPushButtonPECurveClicked)
        self.ui.pushButtonPBCurve.clicked.connect(self.onPushButtonPBCurveClicked)
        self.ui.pushButtonTurnoverRate.clicked.connect(self.onPushButtonTurnoverRateClicked)
        self.ui.pushButtonDividend.clicked.connect(self.onPushButtonDividendClicked)
        self.ui.pushButtonIncomeSheet.clicked.connect(self.onPushButtonIncomeSheetClicked)
        self.ui.pushButtonBalanceSheet.clicked.connect(self.onPushButtonBalanceSheetClicked)
        self.ui.pushButtonCashflowSheet.clicked.connect(self.onPushButtonCashflowSheetClicked)
        self.ui.pushButtonSetPrice.clicked.connect(self.onPushButtonSetPriceClicked)

    def refresh(self):
        print("refresh")
        self.load_my_stock()

    def onTreeWidgetItemClicked(self, item: QTreeWidgetItem, column: int):
        print("onTreeWidgetItemClicked")
        self.current_stock_code = item.text(1)

    def onPushButtonLastMonthClicked(self):
        print("onPushButtonLastMonthClicked")
        self.ui.dateEditFrom.setDate(QDate().currentDate().addMonths(-1))
        self.ui.dateEditTo.setDate(QDate().currentDate())

    def onPushButtonLastThreeMonthsClicked(self):
        print("onPushButtonLastThreeMonthsClicked")
        self.ui.dateEditFrom.setDate(QDate().currentDate().addMonths(-3))
        self.ui.dateEditTo.setDate(QDate().currentDate())

    def onPushButtonSixMonthsClicked(self):
        print("onPushButtonSixMonthsClicked")
        self.ui.dateEditFrom.setDate(QDate().currentDate().addMonths(-6))
        self.ui.dateEditTo.setDate(QDate().currentDate())

    def onPushButtonLastYearClicked(self):
        print("onPushButtonLastYearClicked")
        self.ui.dateEditFrom.setDate(QDate().currentDate().addYears(-1))
        self.ui.dateEditTo.setDate(QDate().currentDate())

    def onPushButtonLastTwoYearsClicked(self):
        print("onPushButtonLastTwoYearsClicked")
        self.ui.dateEditFrom.setDate(QDate().currentDate().addYears(-2))
        self.ui.dateEditTo.setDate(QDate().currentDate())

    def load_my_stock(self):
        print("load_my_stock")
        stocks = toml.load("conf/mystock.toml")['stocks']
        # add stocks to self.ui.treeWidget
        my_stock_price = MyStockPrice()
        for group in stocks.keys():
            print(f"{group=}")
            stock_group = stocks[group]
            root = self.ui.treeWidget
            item = QTreeWidgetItem(root)
            item.setText(0, group)
            for stock in stock_group["names"]:
                child = QTreeWidgetItem(item)
                child.setText(0, stock)
                stock_code = self.tushare.get_stock_code_by_name(stock)
                child.setText(1, stock_code)
                # 当前价格，当前PE，购入价格
                close_price_and_pe = self.tushare.get_close_price(stock_code)
                close_price = close_price_and_pe['close_price']
                child.setText(2, str(close_price))
                pe_ttm = close_price_and_pe['pe_ttm']
                pe_ttm_str = str(pe_ttm)
                stock_price = my_stock_price.get_data_by_stock_code(stock_code)
                if stock_price is not None:
                    low_pe_thresh = stock_price['low_pe_thresh']
                    high_pe_thresh = stock_price['high_pe_thresh']
                    if pe_ttm < low_pe_thresh:
                        pe_ttm_str += " ↓"
                    elif pe_ttm > high_pe_thresh:
                        pe_ttm_str += " ↑"
                    child.setText(4, str(stock_price['bought_price']))
                child.setText(3, pe_ttm_str)

        self.ui.treeWidget.expandAll()

    def show_pe_curve(self, df: pd.DataFrame, new_window=False):
        # depend on self.checked
        if new_window:
            figure = plt.figure(figsize=(10, 4))
        else:
            if self.ui.graphicsView.scene() is not None:
                self.ui.graphicsView.scene().clear()
            figure = Figure(figsize=(10, 4))
        axes = figure.gca()
        axes.plot(df['trade_date'], df['pe_ttm'], label='pe_ttm')
        axes.legend()
        axes.set_title(f"{self.current_stock_code} PE Curve")
        axes.grid(True)

        if new_window:
            plt.show()
        else:
            canvas = FigureCanvas(figure)
            scene = QGraphicsScene()
            self.ui.graphicsView.setScene(scene)
            scene.addWidget(canvas)

    def show_pb_curve(self, df: pd.DataFrame, new_window=False):
        # depend on self.checked
        if new_window:
            figure = plt.figure(figsize=(10, 4))
        else:
            if self.ui.graphicsView.scene() is not None:
                self.ui.graphicsView.scene().clear()
            figure = Figure(figsize=(10, 4))
        axes = figure.gca()
        axes.plot(df['trade_date'], df['pb'], label='pb')
        axes.legend()
        axes.set_title(f"{self.current_stock_code} PB Curve")
        axes.grid(True)

        if new_window:
            plt.show()
        else:
            canvas = FigureCanvas(figure)
            scene = QGraphicsScene()
            self.ui.graphicsView.setScene(scene)
            scene.addWidget(canvas)

    def show_turnover_rate_curve(self, df: pd.DataFrame, new_window=False):
        # depend on self.checked
        if new_window:
            figure = plt.figure(figsize=(10, 4))
        else:
            if self.ui.graphicsView.scene() is not None:
                self.ui.graphicsView.scene().clear()
            figure = Figure(figsize=(10, 4))
        axes = figure.gca()
        axes.plot(df['trade_date'], df['turnover_rate_f'], label='turnover_rate')
        axes.legend()
        axes.set_title(f"{self.current_stock_code} Turnover Rate Curve")
        axes.grid(True)

        if new_window:
            plt.show()
        else:
            canvas = FigureCanvas(figure)
            scene = QGraphicsScene()
            self.ui.graphicsView.setScene(scene)
            scene.addWidget(canvas)

    def onPushButtonPECurveClicked(self):
        print("onPushButtonPECurveClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        start = self.ui.dateEditFrom.date().toString("yyyyMMdd")
        end = self.ui.dateEditTo.date().toString("yyyyMMdd")
        df = self.tushare.get_pe_curve(code, start, end)

        # 绘制市盈率曲线到graphicsView
        self.show_pe_curve(df, True)
        self.show_pe_curve(df)

    def onPushButtonPBCurveClicked(self):
        print("onPushButtonPBCurveClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        start = self.ui.dateEditFrom.date().toString("yyyyMMdd")
        end = self.ui.dateEditTo.date().toString("yyyyMMdd")
        df = self.tushare.get_pb_curve(code, start, end)

        # 绘制市盈率曲线到graphicsView
        self.show_pb_curve(df)

    def onPushButtonTurnoverRateClicked(self):
        print("onPushButtonTurnoverRateClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        start = self.ui.dateEditFrom.date().toString("yyyyMMdd")
        end = self.ui.dateEditTo.date().toString("yyyyMMdd")
        df = self.tushare.get_turnover_rate(code, start, end)

        # 绘制市盈率曲线到graphicsView
        self.show_turnover_rate_curve(df)

    def onPushButtonDividendClicked(self):
        print("onPushButtonDividendClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        df = self.tushare.get_dividend(code)
        # df用Markdown格式输出
        self.ui.textEdit.setText(df.to_markdown())

    def onPushButtonIncomeSheetClicked(self):
        print("onPushButtonIncomeSheetClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        start_date = self.ui.dateEditFrom.date().toString("yyyyMMdd")
        end_date = self.ui.dateEditTo.date().toString("yyyyMMdd")
        df = self.tushare.get_income_sheet(code, start_date, end_date)
        # df用Markdown格式输出
        self.ui.textEdit.setText(df.to_markdown())

    def onPushButtonBalanceSheetClicked(self):
        print("onPushButtonBalanceSheetClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        start_date = self.ui.dateEditFrom.date().toString("yyyyMMdd")
        end_date = self.ui.dateEditTo.date().toString("yyyyMMdd")
        df = self.tushare.get_balance_sheet(code, start_date, end_date)
        # df用Markdown格式输出
        self.ui.textEdit.setText(df.to_markdown())

    def onPushButtonCashflowSheetClicked(self):
        print("onPushButtonCashflowSheetClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        start_date = self.ui.dateEditFrom.date().toString("yyyyMMdd")
        end_date = self.ui.dateEditTo.date().toString("yyyyMMdd")
        df = self.tushare.get_cashflow_sheet(code, start_date, end_date)
        # df用Markdown格式输出
        self.ui.textEdit.setText(df.to_markdown())

    def onPushButtonSetPriceClicked(self):
        print("onPushButtonSetPriceClicked")
        code = self.current_stock_code
        if code is None:
            QMessageBox.warning(self, "警告", "请选择股票")
            return
        dialog = SetPriceDialogImp(code)
        dialog.exec_()
