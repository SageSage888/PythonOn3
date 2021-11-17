import random
import datetime


for i in range(1, 31):
    for j in range(1, 21):
        date = datetime.datetime.strftime(datetime.date(
            2021, random.randint(1, 12), random.randint(1, 28)), '%Y-%m-%d')
        a = (i, random.randint(1, 5), random.randint(1, 10), date)
        print(str(a) + ', ', end='')
