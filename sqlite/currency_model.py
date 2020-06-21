import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'currency_db.db')


class CurrencyDoesNotExits(Exception):
    pass


class CurrencyManager(object):

    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.values = None

    def insert(self, objCurrency):
        sql = f"INSERT INTO currency VALUES ({objCurrency.code}, '{objCurrency.name}', '{objCurrency.symbol}')"
        self.cursor.execute(sql)
        self.connection.commit()

    def select_by_code(self, code):
        sql = f"SELECT * FROM currency WHERE code = {code}"
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if not data:
            raise CurrencyDoesNotExits(f"No existen datos para el code = {code}")
        # Retornamos un objeto de currency con los datos
        return Currency(code=data[0], name=data[1], symbol=data[2])

    def filter(self, **kwargs):
        code = kwargs.get('code')
        name = kwargs.get('name')
        symbol = kwargs.get('symbol')
        condition = ' WHERE '
        add_and = False
        add_condition = False

        if code:
            condition += f"code={code}"
            add_condition = True
            add_and = True
        if name:
            if add_and:
                condition += ' AND '

            condition += f"name='{name}'"
            add_condition = True
            add_and = True
        if symbol:
            if add_and:
                condition += ' AND '
            condition += f"symbol='{symbol}'"
            add_condition = True

        sql = "SELECT * FROM currency"
        if add_condition:
            sql += condition
        self.cursor.execute(sql)
        valuesCurrencies = self.cursor.fetchall()

        currenciesList = []
        for currency in valuesCurrencies:
            objCurrency = Currency(code=currency[0], name=currency[1], symbol=currency[2])
            currenciesList.append(objCurrency)

        if len(currenciesList) < 1:
            raise CurrencyDoesNotExits("No existen datos para los filtros enviados")
        return currenciesList

    def update(self,  objCurrencyNew):
        objCurrencyOld= self.select_by_code(code=objCurrencyNew.code)

        condition = ""
        if objCurrencyOld.name != objCurrencyNew.name:
            condition += f" SET name='{objCurrencyNew.name}' "
        if objCurrencyOld.symbol != objCurrencyNew.symbol:
            condition += f", symbol='{objCurrencyNew.symbol}' "
        if condition:
            sql = f"UPDATE currency {condition} WHERE code = {objCurrencyOld.code}"
            self.cursor.execute(sql)
            self.connection.commit()
        else:
            raise CurrencyDoesNotExits("No se actualizao ningun registro !!!!")

    def delete(self, codeToDelete):
        objToDelete = self.select_by_code(code=codeToDelete)

        sql = f"DELETE FROM currency WHERE code={objToDelete.code}"
        self.cursor.execute(sql)
        self.connection.commit()

    def select(self):
        sql = "SELECT * FROM currency"
        self.cursor.execute(sql)
        self.values = self.cursor.fetchall()
        print(self.values)


class Currency(object):
    "Currency Model"
    objects = CurrencyManager(DB_PATH)

    def __init__(self, code, name, symbol):
        self.code = code
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"{self.name}"


"""
peso_col = Currency(1, 'Peso Colombiano', 'COP')
dollar_usd = Currency(2, 'Dollar Estadounidense', 'USD')
euro = Currency(3, 'Euro', 'EUR')

Currency.objects.insert(peso_col)
Currency.objects.insert(dollar_usd)
Currency.objects.insert(euro)
"""


"""Currency.objects.select()
Currency.objects.filter(code=1)
Currency.objects.filter(symbol='EUR')"""


"""objCurrencyNew = Currency(10, "Peso Colombiano Fullss", 'COP')
Currency.objects.update(objCurrencyNew)
print("#Despues de actualizar#")
Currency.objects.select()"""

Currency.objects.delete(2)
print("#Despues de Eliminar#")
Currency.objects.select()



