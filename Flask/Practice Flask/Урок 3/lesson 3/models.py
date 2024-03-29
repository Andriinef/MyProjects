from peewee import (DateTimeField, DoubleField, IntegerField, Model,
                    SqliteDatabase)
from peewee import datetime as peewee_datetime

db = SqliteDatabase("golden-eye.db")


class XRate(Model):
    class Meta:
        database = db
        db_table = "xrates"
        indexes = ((("from_currency", "to_currency"), True),)

    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    updated = DateTimeField(default=peewee_datetime.datetime.now)

    def __str__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


def init_db():
    db.drop_tables(XRate)
    XRate.create_table()
    XRate.create(from_currency=840, to_currency=980, rate=1)
    print("db created!")
