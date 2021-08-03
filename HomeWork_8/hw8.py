<<<<<<< HEAD
from datetime import datetime, timedelta

days = {'Tuesday': timedelta(days=1), 'Wednesday': timedelta(days=2), 'Thursday': timedelta(
    days=3), 'Friday': timedelta(days=4), 'Saturday': timedelta(days=2), 'Sunday': timedelta(days=1)}


def congratulate(users):
    cur = datetime.now()
    # cur = datetime(year=2021, month=8, day=2)  # fake monday

    prep = {'Monday': '', 'Tuesday': '',
            'Wednesday': '', 'Thursday': '', 'Friday': ''}

    if cur.strftime('%A') == 'Monday':
        for i in users:
            check_date = (i['birthday'].date())

            if check_date.strftime('%m %d') == cur.strftime('%m %d'):  # monday list
                prep['Monday'] += (i['name']) + ', '
            # monday list
            elif (cur.date() - days['Saturday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Monday'] += (i['name']) + ', '
            # monday list
            elif (cur.date() - days['Sunday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Monday'] += (i['name']) + ', '
            elif (cur.date() + days['Tuesday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Tuesday'] += (i['name']) + ', '
            elif (cur.date() + days['Wednesday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Wednesday'] += (i['name']) + ', '
            elif (cur.date() + days['Thursday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Thursday'] += (i['name']) + ', '
            elif (cur.date() + days['Friday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Friday'] += (i['name']) + ', '
    return send_msg(prep)


def send_msg(persons):
    for k, v in persons.items():
        print(f'{k}: {v[:-2]}', end='\n')


congratulate([{'name': 'Kirill', 'birthday': datetime(year=1987, month=8, day=5)},
              {'name': 'Dima', 'birthday': datetime(
                  year=1990, month=8, day=4)},
              {'name': 'Olya', 'birthday': datetime(
                  year=1994, month=8, day=3)},
              {'name': 'Test', 'birthday': datetime(
                  year=1987, month=7, day=31)},
              {'name': 'Gosha', 'birthday': datetime(
                  year=1991, month=8, day=1)},
              {'name': 'Misha', 'birthday': datetime(year=1995, month=8, day=2)}])
=======
from datetime import datetime, timedelta

days = {'Tuesday': timedelta(days=1), 'Wednesday': timedelta(days=2), 'Thursday': timedelta(
    days=3), 'Friday': timedelta(days=4), 'Saturday': timedelta(days=2), 'Sunday': timedelta(days=1)}


def congratulate(users):
    #cur = datetime.now()
    cur = datetime(year=2021, month=8, day=2)  # fake monday

    prep = {'Monday': '', 'Tuesday': '',
            'Wednesday': '', 'Thursday': '', 'Friday': ''}

    if cur.strftime('%A') == 'Monday':
        for i in users:
            check_date = (i['birthday'].date())

            if check_date.strftime('%m %d') == cur.strftime('%m %d'):  # monday list
                prep['Monday'] += (i['name']) + ', '
            # monday list
            elif (cur.date() - days['Saturday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Monday'] += (i['name']) + ', '
            # monday list
            elif (cur.date() - days['Sunday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Monday'] += (i['name']) + ', '
            elif (cur.date() + days['Tuesday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Tuesday'] += (i['name']) + ', '
            elif (cur.date() + days['Wednesday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Wednesday'] += (i['name']) + ', '
            elif (cur.date() + days['Thursday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Thursday'] += (i['name']) + ', '
            elif (cur.date() + days['Friday']).strftime('%m %d') == check_date.strftime('%m %d'):
                prep['Friday'] += (i['name']) + ', '
    return send_msg(prep)


def send_msg(persons):
    for k, v in persons.items():
        print(f'{k}: {v[:-2]}', end='\n')


congratulate([{'name': 'Kirill', 'birthday': datetime(year=1987, month=8, day=5)},
              {'name': 'Dima', 'birthday': datetime(
                  year=1990, month=8, day=4)},
              {'name': 'Olya', 'birthday': datetime(
                  year=1994, month=8, day=3)},
              {'name': 'Test', 'birthday': datetime(
                  year=1987, month=7, day=31)},
              {'name': 'Gosha', 'birthday': datetime(
                  year=1991, month=8, day=1)},
              {'name': 'Misha', 'birthday': datetime(year=1995, month=8, day=2)}])
>>>>>>> 037c4d88185f51b915bb3be8f3da35867d0a1dae
