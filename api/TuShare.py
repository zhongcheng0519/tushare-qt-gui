import tushare as ts
import pandas as pd
import toml


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


