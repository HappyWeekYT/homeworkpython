from datetime import datetime


from datetime import date, timedelta

def mamontenok_capitan(zapisi, date):
    vremya = timedelta(days=1)
    dnevnik = open('zapisi.txt', 'w')
    for zapis in zapisi:
        dnevnik.write(str(date) +': '+zapis+'\n')
        date+=vremya
    dnevnik.close()

mamontenok_capitan(['privet', 'kak dela', 'poka'], date(1980, 3, 12))
