import tushare as ts
import pandas as pd
import toml
from datetime import datetime


class TuShare:

    def __init__(self):
        self.TOKEN = toml.load("conf/secret.toml")["tushare_token"]
        ts.set_token(self.TOKEN)
        self.pro = ts.pro_api()
        self.stocks = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,name')
        self.stocks = self.stocks.set_index('ts_code')

    def get_stock_code_by_name(self, name: str) -> str:
        return self.stocks[self.stocks['name'] == name].index[0]

    def get_pe_curve(self, code: str, start: str, end: str) -> pd.DataFrame:
        df = self.pro.daily_basic(ts_code=code, start_date=start, end_date=end, fields='trade_date,pe_ttm')
        # 转换日期格式
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        return df

    def get_pb_curve(self, code: str, start: str, end: str) -> pd.DataFrame:
        df = self.pro.daily_basic(ts_code=code, start_date=start, end_date=end, fields='trade_date,pb')
        # 转换日期格式
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        return df

    def get_turnover_rate(self, code: str, start: str, end: str) -> pd.DataFrame:
        df = self.pro.daily_basic(ts_code=code, start_date=start, end_date=end, fields='trade_date,turnover_rate_f')
        # 转换日期格式
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        return df

    def get_dividend(self, code: str) -> pd.DataFrame:
        df = self.pro.dividend(ts_code=code, fields='ts_code,div_proc,stk_div,cash_div_tax,record_date,ex_date')
        return df

    def get_income_sheet(self, code: str, start: str, end: str) -> pd.DataFrame:
        df = self.pro.income(ts_code=code, start_date=start, end_date=end, fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,total_profit,n_income')
        return df

    def get_balance_sheet(self, code: str, start: str, end: str) -> pd.DataFrame:
        df = self.pro.balancesheet(ts_code=code, start_date=start, end_date=end, fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,cap_rese,accounts_receiv_bill,accounts_pay')
        return df

    def get_cashflow_sheet(self, code: str, start: str, end: str) -> pd.DataFrame:
        df = self.pro.cashflow(ts_code=code, start_date=start, end_date=end, fields='ts_code,end_date,net_profit,c_paid_for_taxes')
        return df

    def get_close_price(self, code: str) -> float:
        today = datetime.today().strftime('%Y%m%d')
        yesterday = (datetime.today() - pd.Timedelta(days=1)).strftime('%Y%m%d')
        now = datetime.now()
        if now.hour < 15:
            trade_date = yesterday
        else:
            trade_date = today
        df_daily = self.pro.daily(ts_code=code, trade_date=trade_date, fields='ts_code,trade_date,close')
        df_daily_basic = self.pro.daily_basic(ts_code=code, trade_date=trade_date, fields='ts_code,trade_date,pe_ttm')
        res = {
            "close_price": df_daily['close'][0],
            "pe_ttm": df_daily_basic['pe_ttm'][0]
        }
        return res
