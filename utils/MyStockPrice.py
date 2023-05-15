import sqlite3


class MyStockPrice:
    def __init__(self):
        self.conn = sqlite3.connect('db/my_stock_price.db')
        self.cursor = self.conn.cursor()
        self.table_name = 'my_stock_price'
        self.create_table()

    def create_table(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} (stock_code LINESTRING PRIMARY KEY, bought_price REAL, high_pe_thresh REAL, low_pe_thresh REAL)"
        self.cursor.execute(sql)
        self.conn.commit()

    def get_data_by_stock_code(self, stock_code: str):
        # 查询数据
        self.cursor.execute(f'SELECT bought_price, high_pe_thresh, low_pe_thresh FROM {self.table_name} WHERE stock_code="{stock_code}"')
        data = self.cursor.fetchone()

        if data is not None:
            # 如果找到数据，则返回 datetime 和 motorTorqueMean
            return {'bought_price': data[0], 'high_pe_thresh': data[1], 'low_pe_thresh': data[2]}
        else:
            # 如果未找到数据，则返回 None
            return None

    def insert_data(self, stock_code: str, bought_price: float, high_pe_thresh: float, low_pe_thresh: float):
        # 检查是否存在此 stock_code
        self.cursor.execute(f'SELECT stock_code FROM {self.table_name} WHERE stock_code="{stock_code}"')
        data = self.cursor.fetchone()

        if data is None:
            # 如果 stock_code 不存在，则插入新数据
            sql = f'INSERT INTO {self.table_name} (stock_code, bought_price, high_pe_thresh, low_pe_thresh) VALUES ("{stock_code}", {bought_price}, {high_pe_thresh}, {low_pe_thresh})'
            print(sql)
            self.cursor.execute(sql)
        else:
            # 如果 stock_code 已存在，则更新数据
            sql = f'UPDATE {self.table_name} SET bought_price={bought_price}, high_pe_thresh={high_pe_thresh}, low_pe_thresh={low_pe_thresh} WHERE stock_code="{stock_code}"'
            print(sql)
            self.cursor.execute(sql)
        self.conn.commit()

    def __del__(self):
        # 关闭连接
        self.conn.close()
