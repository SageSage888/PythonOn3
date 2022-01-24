import aiohttp
import asyncio
from bs4 import BeautifulSoup
import sqlite3


def insert_multiple_records(url, record):
    records = (url, record)
    print(records)
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS lun (url, info)")
        cursor.execute("""INSERT INTO lun
                                 (url, info)
                                 VALUES (?, ?);""", records)

        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


async def func1():
    async with aiohttp.ClientSession() as session:
        url = "https://coincost.net/uk/currency/terra-luna"
        async with session.get(url) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find(
                'div', class_="cryptocurrency-dynamics wide").find('p').text
            insert_multiple_records(url, result)
            print(result)
            return result


async def func2():
    async with aiohttp.ClientSession() as session:
        url = "https://coinmarketcap.com/currencies/terra-luna/"
        async with session.get(url) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find(
                'div', class_="priceValue").find('span').text.replace('$', '')
            insert_multiple_records(url, result)
            print(result)
            return result


""" async def func3():
    async with aiohttp.ClientSession() as session:
        url = "https://cryptorank.io/ru/price/luna"
        async with session.get(url) as response:
            text = await response.read()
            result = BeautifulSoup(text.content, "html.parser").find(
                'div', class_="styled__CoinPrice-sc-9jm877-5 jUaGuT").text.replace('USD ', '')
            insert_multiple_records(result)
            print(result)
            return result """


async def main():
    sites_soup = asyncio.gather(func1(), func2())
    await sites_soup


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
