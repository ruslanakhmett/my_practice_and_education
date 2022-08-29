import csv
from peewee import *


db = PostgresqlDatabase(database='test3', user='postgres', password='123456789wW', host='localhost')

class Coin(Model):
    name = CharField(max_length=50)
    price = TextField()
    url = CharField()

    class Meta:
        database = db


def main():

    db.connect()
    db.create_tables([Coin])

    with open('cmc.csv') as f:
        order = ['name', 'price', 'url']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        with db.atomic():
            # for row in coins: (еще один способ, менее быстрый)
            #     Coin.create(**row)
            for index in range(0, len(coins), 100):
                Coin.insert_many(coins[index:index+100]).execute()


if __name__ == '__main__':
    main()