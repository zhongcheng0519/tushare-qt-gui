from GUI.basic.SetPriceDialog import *
from utils.MyStockPrice import MyStockPrice


class SetPriceDialogImp(QDialog):

    def __init__(self, stock_code: str):
        super(SetPriceDialogImp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.labelStockName.setText(stock_code)
        self.db = MyStockPrice()
        res = self.db.get_data_by_stock_code(stock_code)
        if res is not None:
            self.ui.doubleSpinBoxBoughtPrice.setValue(res['bought_price'])
            self.ui.doubleSpinBoxHighPEThresh.setValue(res['high_pe_thresh'])
            self.ui.doubleSpinBoxLowPEThresh.setValue(res['low_pe_thresh'])

    def accept(self):
        stock_code = self.ui.labelStockName.text()
        bought_price = self.ui.doubleSpinBoxBoughtPrice.value()
        high_pe_thresh = self.ui.doubleSpinBoxHighPEThresh.value()
        low_pe_thresh = self.ui.doubleSpinBoxLowPEThresh.value()
        self.db.insert_data(stock_code, bought_price, high_pe_thresh, low_pe_thresh)
        super().accept()
