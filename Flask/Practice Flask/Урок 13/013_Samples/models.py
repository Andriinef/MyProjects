import config
from peewee import (CharField, DateTimeField, DoubleField, IntegerField, Model,
                    SqliteDatabase, TextField)
from peewee import datetime as peewee_datetime

db = SqliteDatabase(config.DB_NAME)


class _Model(Model):
    class Meta:
        database = db

    def json(self):
        return self.__data__


class XRate(_Model):
    class Meta:
        db_table = "xrates"
        indexes = ((("from_currency", "to_currency"), True),)

    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    updated = DateTimeField(default=peewee_datetime.datetime.now)
    module = CharField(max_length=100)

    def __str__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


class ApiLog(_Model):
    class Meta:
        db_table = "api_logs"

    request_url = CharField()
    request_data = TextField(null=True)
    request_method = CharField(max_length=100)
    request_headers = TextField(null=True)
    response_text = TextField(null=True)
    created = DateTimeField(index=True, default=peewee_datetime.datetime.now)
    finished = DateTimeField()
    error = TextField(null=True)


class ErrorLog(_Model):
    class Meta:
        db_table = "error_logs"

    request_data = TextField(null=True)
    request_url = TextField()
    request_method = CharField(max_length=100)
    error = TextField()
    traceback = TextField(null=True)
    created = DateTimeField(default=peewee_datetime.datetime.now, index=True)


def init_db():
    XRate.drop_table()
    XRate.create_table()
    XRate.create(from_currency=840, to_currency=980, rate=1, module="privat_api")
    XRate.create(from_currency=840, to_currency=643, rate=1, module="cbr_api")
    XRate.create(from_currency=1000, to_currency=840, rate=1, module="privat_api")
    XRate.create(from_currency=1000, to_currency=980, rate=1, module="cryptonator_api")
    XRate.create(from_currency=1000, to_currency=643, rate=1, module="cryptonator_api")

    for m in (ApiLog, ErrorLog):
        m.drop_table()
        m.create_table()

    print("db created!")
