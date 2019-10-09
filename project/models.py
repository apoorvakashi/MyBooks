from peewee import *

db = SqliteDatabase('my_books.db')


class User(Model):
    name = CharField()

    class Meta:
        database = db


class Book(Model):
    name = CharField()
    author = CharField()
    genre = CharField()
    year = IntegerField(default  = 0)
    rating = DecimalField(default=0)
    is_read = BooleanField()
    is_fav = BooleanField()
    owner = ForeignKeyField(User, backref="books")

    class Meta:
        database = db


if __name__ == "__main__":
    db.connect()
    db.create_tables([User, Book])

